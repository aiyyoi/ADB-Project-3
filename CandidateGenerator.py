'''
Candidate k-itemset generator
from large (k-1)-itemset
'''

import copy

class Generator:
	'''
		takes key set of priLargeItemset dictionary (each key is a set in datastructure)
		returns key set of candidate itemset
	'''
		

	def genCandidate(self, priLargeItemset):
		self.priLargeItemset = priLargeItemset
		curCandidateItemset = []
		k = len(self.priLargeItemset[0])
		print 'Generating candidates at k = '+ str(k+1)
		maxIter = len(self.priLargeItemset)
		#join step
		if k<2:
			for i in range(maxIter):
				for j in range(i+1, maxIter):
					cp = copy.deepcopy(self.priLargeItemset[i])
					cp.extend(self.priLargeItemset[j])
					newCandidate = set(cp)
					curCandidateItemset.append(newCandidate)
		else:
			for i in range(maxIter):
				common = list(self.priLargeItemset[i])[:k-1]
				for j in range(i+1, maxIter):
					cp = copy.deepcopy(self.priLargeItemset[i])
					if set(common).issubset( self.priLargeItemset[j] ):
						cp.update(self.priLargeItemset[j])
						if len(cp) == (k+1) and self.prune(cp) and cp not in curCandidateItemset:
							curCandidateItemset.append(cp)
		return curCandidateItemset

		

	def prune(self, newCandidate):
		# prune step
		for i in range(len(newCandidate)):
			toCheck = list(newCandidate)
			toCheck.pop(i)
			if set(toCheck) in self.priLargeItemset:
				return True
			else:
				return False


