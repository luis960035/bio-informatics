from collections import Counter
#Calculates GC content
seq = open ("sequence.fasta","r");
dict = Counter()
for line in seq:
		line = line.lower()
		dict['g'] += line.count("g")
		dict['c'] += line.count('c')
		dict['a'] += line.count('a')
		dict['t'] += line.count('t')
for item in dict.items():
	print "appearances of "+str(item[0])+" : "+str(item[1])
print
gc = (dict['g'] + dict['c']) / (1.0* sum(dict.values()))
print "GC-content : "'%f' %(gc*100.0)+" %" 