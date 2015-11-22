'''
	Main business logic implementation 
	For ADB Project3
	Reads in data from file, parse inputs
	Delegate to suitable classes for analysis
'''

import argparse
import csv

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
print minSup
print minConf

#collection of market baskets
baskets = []

with open(filePath, 'rU') as csvFile:
	fileReader = csv.reader(csvFile, delimiter = ',', quotechar = '"')
	for row in fileReader:
		baskets.append(row)

# should skip first row
i = 1
while i<10:
	print ','.join(baskets[i])
	print '\n'
	i += 1
