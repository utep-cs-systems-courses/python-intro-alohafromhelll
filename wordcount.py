#Jerardo Velazquez
import sys
import string
import re

#get command line arguments
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#open file for writing output
out_file = open(outputfile, 'w')

#open input file
f = open(inputfile, "r")

#creating a dictionary for the words
wordsdict = dict()

#reading data from file
for line in f:
	#remove newline characters
	line = line.strip()
	#lower case
	line = line.lower()
	#split by punctuation and space
	s = re.split('\W+', line)
	#remove remaining white space
	s = filter(None, s)

	#adding word to dictionary
	for word in s:
		if word not in wordsdict:
			wordsdict[word] = 1
		else:
			wordsdict[word] += 1

#printing to output file
for key, value in sorted(wordsdict.items()):
	print("{} {}".format(key, value), file = out_file)
