'''
	Main business logic implementation 
	For ADB Project3
	Reads in data from file, parse inputs
	Delegate to suitable classes for analysis
'''

import argparse
import csv
import math
import Apriori


#################### New Classification, Sampling and Summary Session #################################
parser = argparse.ArgumentParser(prog='ADB Project 3', description = 'how to use the script')
parser.add_argument('-data', help = 'file path to static dataset', required = True)
parser.add_argument('-msup', help = 'minimum support threshold', required = True)
parser.add_argument('-mconf', help = 'minimum confidence threshold', required = True)
args = parser.parse_args()

filePath = args.data
minSup = float(args.msup)
minConf = float(args.mconf)

print "filePath: "+ filePath
#collection of market baskets: (TID: [items])
baskets = {}

with open(filePath, 'rU') as csvFile:
	fileReader = csv.reader(csvFile, delimiter = ',', quotechar = '"')
	i = 0
	for row in fileReader:
		baskets[i] = row
		i+=1

# should skip first row
baskets.pop(0)
## changed into absolute minimum support and confidence count
minSup = math.floor(len(baskets)*minSup)
minConf = math.floor(len(baskets)*minConf)
print 'Absolute minimum support count: '+ str(minSup)
print 'Absolute minimum confidence count: ' + str(minConf)

# transform baskets to initial large 1-itemset
iniItemSet = list(set().union(*baskets.values()))
iniCanItemset = []
for item in iniItemSet:
	if item != '' and item is not None:
		iniCanItemset.append([item])
print 'Generating set of large itemsets ...'

apriori = Apriori.AprioriInstance(baskets, minSup, iniCanItemset)
answer = apriori.aprioriLogic()

print '='*20
for each in answer:
	print each


# Generate Association rules