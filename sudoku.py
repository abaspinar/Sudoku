import sys
def solve(inList,row,col):
	for r in range(row,9):
		for c in range(col,9):
			if inList[r][c] == '0':
				num = 1
				while num < 10:
					n = str(num)
					#checks if n is unique in row, column or containing 3x3 box
					if n in inList[r] or n in [inList[x][c] for x in range(0,9)]\
							or n in [inList[x][y] for x in range(3*((r)/3),3*((r)/3)+3)\
							for y in range(3*((c)/3),3*((c)/3)+3)]:
								num += 1
					else:
						inList[r][c] = n
						outList = solve(inList,r,c)
            					if outList == -1:
							inList[r][c] = '0'
							num += 1
            					else:
		    					break
        			if num == 10:
          				return -1
    		col = 0
  	return inList

def usage():
	print "Usage python sudoku.py [input file]"

def readFile(inputFile):
	try:
		filehnd = open(inputFile)
		inList = []
		for line in filehnd.readlines():
			m = line.strip().split(',')
			if len(m) != 9:
				print "Wrong file format!"
				filehnd.close()
				return -1
			else:
				inList.append(m)
		filehnd.close()
		if len(inList) != 9:
			print "Wrong file format!"
			return -1
		return inList
	except:
		print "Could not open the file %s" % (inputFile)
		return -1

def writeFile(outputFile,outList):
	try:
		filehnd = open(outputFile,'w')
		for i in outList:
			filehnd.writelines("%s\n" % (','.join(i)))
		filehnd.close()
		return True
	except:
		print "Could not open the file %s" % (outputFile)
		return False

def main(inputFile):
	inList = readFile(inputFile)
	if inList == -1:
		sys.exit(1)
	else:
		outList = solve(inList,0,0)
		if outList == -1:
			print "Could not solve the sudoku given!"
			sys.exit(1)
		else:
			outputFile = "%s_out.csv" % (inputFile.split(".csv")[0])
			check = writeFile(outputFile,outList)
			if check:
				print "Sudoku solved and the file %s created." % (outputFile)
				sys.exit(0)
if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()
	else:
		main(sys.argv[1])
