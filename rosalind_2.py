from collections import Counter
import sys
if len(sys.argv) == 1:
	filename = "rosalind2.txt"
else :
	filename = sys.argv[1]
seq = open (filename,"r").read();
dict = Counter()
for base in seq:
	if base == "T":
		base = "U";
	elif base == "U":
		base = "T";
	sys.stdout.write(base)
	sys.stdout.flush()