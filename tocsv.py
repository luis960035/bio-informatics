import sys
import os.path#for splitext aka to get the file extension of the given file



def main():   
	
	if len(sys.argv) == 1:
		print "no argument file given"
		print "...Abort"
		return 0


	filename = sys.argv[1]
	print "open file:"+filename
	input = open(filename,"r")
	
	extension = os.path.splitext(filename)[1]
	if extension == ".csv" :
		print "given file is allready in .csv format"
		print "...Abort"
		input.close()
		return 0

	
	output_file = sys.argv[1] + ".csv"
	print "send to file:"+output_file
	output = open(output_file,"w")
	
	line_count = 0
	if len(sys.argv) > 2 :
		for i in xrange (0,int(sys.argv[2])):
			output.write(input.readline())
			line_count += 1
	
	for line in  input:
		line_count+=1
		index = 0
		for char in line:
			index+=1
			output.write(char)
			if len(line) != index and (len(line)-1 != index or line[index]!='\n'):
				output.write(",")
		
		print '.',	
	input.close()
	output.close()
	
	print "Done"
	print "Transformed "+str(line_count)+" lines to .csv format"
	


if __name__ == "__main__":
	main()