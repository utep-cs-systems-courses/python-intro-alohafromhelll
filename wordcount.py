import sys
import string
import re
#take input of in and output file
#no whitespace
#case-insensitive


inputfile = sys.argv[1]
outputfile = sys.argv[2]

out_file = open(outputfile, 'w')


f = open(inputfile, "r")

wordsdict = dict()

#print(f)

for line in f:

	line = line.strip()

	line = line.lower()

	s = re.split('\W+', line)

	s = filter(None, s)

	print(s)


	for word in s:
		if word not in wordsdict:
			wordsdict[word] = 1
		else:
			wordsdict[word] += 1




for key, value in sorted(wordsdict.items()):
	print("{} : {}".format(key, value), file = out_file)
