from collections import Counter
import sys
if len(sys.argv) == 1:
	filename = "rosalind3.txt"
else :
	filename = sys.argv[1]
seq = open (filename,"r").read();
output = []
for base in seq:
	if base == 'A':
		base = 'T';
	elif base == 'T':
		base = 'A'
	elif base == 'G':
		base = 'C';
	elif base == 'C':
		base = 'G';	
	else:
		continue
	output.append(base)
output.reverse()
for base in output:
	sys.stdout.write(base)
	sys.stdout.flush()
