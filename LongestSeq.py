import sys
from collections import Counter
def main():   
	k = 7	
	if len(sys.argv) == 1:
		print "no argument file given"
		print "...Abort"
		return 0
	filename = sys.argv[1]
	if len(sys.argv) == 3:
		k = int(sys.argv[2])
	File = open(filename,"r")
	File.readline()
	Text = File.read()
	dict = Counter()
	Text = ''.join(Text.split())#remove white spaces
	for x in xrange(0,len(Text),k):
		pattern = Text[x:x+k]		
		for y in xrange(0,len(Text),k):
			seq = Text[y:y+k]
			if seq == pattern:
				print seq
				print ""
				dict[seq] += 1
	
	longest_seq = max(dict)
	max_appearances = dict[max(dict)]
	if(max_appearances == 1):
		print 'All sequences have the same length'
	else:
		print 'Max appearances '+str(max_appearances) + ":"
		for item in dict.items():
			if item[1] == max_appearances:
				print item[0]

if __name__ == "__main__":
	main()