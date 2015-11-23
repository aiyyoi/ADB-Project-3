'''
Takes in candidate itemsets and produce large itemsets
Needs market baskets and minimum support as parameters
'''
import MemberClass

class ItemsetGenerator:
	def __init__(self, canItemset, baskets, minSup):
		self.candidateSet = [] # keeps each itemset member, count 0 at initialization
		for eachSet in canItemset:
			self.candidateSet.append(MemberClass.Member(eachSet))
		self.baskets = baskets
		self.minSup = minSup


	def genLargeItemset(self):
		# update support counts for each candidate itemset
		largeItemset = [] # the keyset of large itemset
		for eachMember in self.candidateSet:
			count = sum(set(eachMember.getItemSet()).issubset(eachTransaction) for eachTransaction in self.baskets.values())
			eachMember.setSupportCount(count)
			if eachMember.getSupportCount()>self.minSup:
				print ', '.join(eachMember.getItemSet()) + ' : '+ str(eachMember.getSupportCount())
				largeItemset.append(eachMember.getItemSet())
		return largeItemset