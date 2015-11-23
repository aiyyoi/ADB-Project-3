'''
Candidate k-itemset generator
from large (k-1)-itemset
'''


class Generator:
	'''
		takes key set of priLargeItemset dictionary (each key is a set in datastructure)
		returns key set of candidate itemset
	'''
	def __init__(self, priLargeItemset):
		self.priLargeItemset = priLargeItemset

	def genCandidate(self):
		curCandidateItemset = []
		k = len(self.priLargeItemset[0])
		maxIter = len(self.priLargeItemset)
		#join step
		if k<2:
			for i in range(maxIter):
				cp = self.priLargeItemset[i]
				#print cp
				for j in range(i+1, maxIter):
					cp.extend(self.priLargeItemset[j])
					newCandidate = set(cp)
					curCandidateItemset.append(newCandidate)
		else:
			for i in range(maxIter):
				common = list(self.priLargeItemset[i])[:k-1]
				cp = self.priLargeItemset[i]
				for j in range(i+1, maxIter):
					if common in self.priLargeItemset[j]:
						newCandidate = cp.update(self.priLargeItemset[j])
						if len(newCandidate) == (k+1) and self.prune(newCandidate):
							curCandidateItemset.append(newCandidate)
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


