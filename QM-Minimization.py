def stripTerms(input):
	mEnd = False
	dStart = False
	dEnd = False
	mTerms = []
	dTerms = []
	check = False
	for i in range(len(input)):
		if(check):
			check = False
			continue
		if(i == 0 and input[i] != 'm'):
			print("incorrect input format")
			return None, None
		if(i == 1 and input[i] != '('):
			print("incorrect input format")
			return None, None
		if(i > 1 and input[i] == ")"):
			mEnd = True; 
		if(i > 1 and mEnd == False):
			if(input[i]==","):
				continue 
			elif(i < len(input)-1 and input[i+1]!= "(" and input[i+1]!= ")" and input[i+1]!= "+" and input[i+1]!= ","): 
				mTerms.append(int(input[i]+input[i+1]))
				check = True
			else: 
				mTerms.append(int(input[i]))
		if(mEnd):
			if(input[i] == "d"):
				dStart = True 
				continue
			if(dStart): 
				if(input[i]=="(" or input[i]=="," or input[i]=="+"):
					continue
				elif(input[i]==")"):
					dEnd = True 
					break 
				else:
					dTerms.append(int(input[i]))
	return mTerms, dTerms
def CreateBinaryStrings(mTerms, dTerms):
	mBinary = []
	dBinary = []
	for i in range(len(mTerms)):
		if(len("{0:b}".format(mTerms[i]))<4): 
		#	mBinary.append((4-len))
		#mBinary.append("{0:b}".format(mTerms[i]))
			diff = 4 - len("{0:b}".format(mTerms[i]))
			newString = "0"*diff
			mBinary.append(newString + "{0:b}".format(mTerms[i])) 
		else: 
			mBinary.append("{0:b}".format(mTerms[i]))
		#print(mTerms[i])
		#print(mBinary[i])
	for i in range(len(dTerms)):
		if(len("{0:b}".format(mTerms[i]))<4): 
		#	mBinary.append((4-len))
		#mBinary.append("{0:b}".format(mTerms[i]))
			diff = 4 - len("{0:b}".format(dTerms[i]))
			newString = "0"*diff
			dBinary.append(newString + "{0:b}".format(dTerms[i])) 
		else: 
			dBinary.append("{0:b}".format(dTerms[i]))
	return mBinary, dBinary
		#print(dTerms[i])
		#print(dBinary[i])
#	for i in range(len(mTerms)):
#		print(mTerms[i])
#		print(" ")
#	for i in range(len(dTerms)):
#		print(dTerms[i])
#		print(" ")
mInput, dInput = stripTerms("m(1,2,3,9,10)+d(5,7)")
mBinary, dBinary = CreateBinaryStrings(mInput, dInput)