import sys
from collections import Counter
if len(sys.argv) == 1:
	filename = "rosalind1.txt"
else :
	filename = sys.argv[1]
seq = open (filename,"r").read();
dict = Counter()
dict['A'] = seq.count("A")
dict['C'] = seq.count('C')
dict['G'] = seq.count('G')
dict['T'] = seq.count('T')

for item in dict.items():
	print "appearances of "+str(item[0])+" : "+str(item[1])