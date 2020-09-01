import sys
import string
#take input of in and output file
#no whitespace
#case-insensitive



#with open('declaration.txt', 'r') as f:
	#all_lines = f.readlines()

#if len(sys.argv) == 2:
inputfile = sys.argv[1]
outputfile = sys.argv[2]

out_file = open(outputfile, 'w')





f = open(inputfile, "r")

wordsdict = dict()

#print(f)

for line in f:

	line = line.strip()

	line = line.lower()



	line = line.translate(line.maketrans("", "", string.punctuation))

	s = line.split(" ")
	print(s)



	for word in s:
		if word not in wordsdict:
			wordsdict[word] = 1
		else:
			wordsdict[word] += 1




for key, value in sorted(wordsdict.items()):
	print("{} : {}".format(key, value), file = out_file)

#print(wordsdict, file = out_file)
#out_file.close()


#for key in list(d.keys()):
#	print(key, ":", d[key])
