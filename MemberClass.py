'''
Class of itemset member (member of Lk or Ck),
has two field:
1) itemset list
2) absolute support count

'''

class Member:
	def __init__(self, itemSet, count = 0):
		self.itemSet = itemSet
		self.supCnt = count

	def getItemSet(self):
		return self.itemSet

	def getSupportCount(self):
		return self.supCnt

	def setSupportCount(self, cnt):
		self.supCnt = cnt