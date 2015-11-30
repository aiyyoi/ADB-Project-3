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
import itertools

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
minSup = len(baskets)*minSup
print 'Absolute minimum support count: '+ str(minSup)
print 'Minimum confidence: ' + str(minConf)

# transform baskets to initial large 1-itemset
iniItemSet = list(set().union(*baskets.values()))
iniCanItemset = []
for item in iniItemSet:
	if item != '' and item is not None:
		iniCanItemset.append([item])
print 'Generating set of large itemsets ...'

apriori = Apriori.AprioriInstance(baskets, minSup, iniCanItemset)
answer = apriori.aprioriLogic()



output = open('output.txt', 'w')
output.write( "\n===Frequent itemsets (min_sup=" + str(minSup * 100/len(baskets)) + "%)\n\n" )
for each in answer:
	output.write( "[" + ', '.join(each.getItemSet()) + "]" + ' support: '+ str(float(each.getSupportCount() * 100)/len(baskets)) + "%\n")

output.write( "\n===High-confidence association rules (min_conf=" + str(minConf*100) + "%)\n\n" )

# Generate Association rules
for a in answer:
	for i in range(1,len(a.getItemSet())):
		S = set(a.getItemSet())
		sub =  set(itertools.combinations(S, i))
		for s in sub:
			diff = S.difference(s)
			if len(diff) != 1:
				continue	
			sup_l = a.getSupportCount()
			sup_subs = 0
			flag1 = 0
		
			for j in answer:	
				if set(j.getItemSet()) == set(s):
					sup_subs = j.getSupportCount()	
					flag1 = 1	
				if flag1 == 1:
					break

			if float(sup_l) / sup_subs >= minConf:
				output.write( "[" + ', '.join(s) +  "]" + " => " + "[" + ', '.join(diff) + "] (Conf: " + str(float(sup_l) * 100 / sup_subs) + "%, Supp: " + str(float(sup_l) * 100 /len(baskets)) + "%)\n" )

output.close()
