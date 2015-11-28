'''
Aprioi logic in Figure 1 from reference
'''

import CandidateGenerator
import LargeItemsetGenerator

class AprioriInstance:
	def __init__(self, baskets, minSup, iniCanItemset):
		self.largeItemsetGenerator = LargeItemsetGenerator.ItemsetGenerator(baskets, minSup)
		self.canItemsetGenerator = CandidateGenerator.Generator()
		self.iniLargeItemset = self.largeItemsetGenerator.genLargeItemset(iniCanItemset)

	def aprioriLogic(self):
		answer = [] # all large itemsets found are to be appended
		ptLargeItemset = self.iniLargeItemset
		answer.extend(self.iniLargeItemset)
		while len(ptLargeItemset) >0:
			last = []
			for eachMember in ptLargeItemset:
				last.append(eachMember.getItemSet())
			canItemset = self.canItemsetGenerator.genCandidate(last)
			ptLargeItemset = self.largeItemsetGenerator.genLargeItemset(canItemset)
			if len(ptLargeItemset)>0:
				answer.extend(ptLargeItemset)
			else:
				print 'No more large itemsets...'

		return answer