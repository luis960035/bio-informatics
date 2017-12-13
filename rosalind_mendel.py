from collections import Counter
import sys

def main():
	if len(sys.argv) == 1:
		filename = "test.txt"
	else :
		filename = sys.argv[1]
	seq = open (filename,"r").read();
	numbers = map(int,seq.split())
	output = []

	k = numbers[0]
	m = numbers[1]
	n = numbers[2]

	total = k + m + n

	selectk = (k*1.0)/total 
	selectm = (m*1.0)/total 
	selectn = (n*1.0)/total

	total-=1
	selectk2 = (k*1.0)/total 
	selectm2 = (m*1.0)/total 
	selectn2 = (n*1.0)/total

	probk = selectk
	probm = selectm * (0.75*(((m-1)*1.0)/total)+  0.5*selectn2 + selectk2)
	probn = selectn * ( 0.5*selectm2 + selectk2)
	prob = probk + probm + probn 

	print "%.5f"%prob

if __name__ == '__main__':
	main()