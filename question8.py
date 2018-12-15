def patternMatcher(pattern, string):
	
	#check if the first element is x if not swap and keep tracked if its swapped or not
	new_pattern=''
	toggled=False
	if(pattern[0]=='y'):
		toggled=True
		for ch in pattern:
			if(ch=='x'):
				new_pattern=new_pattern+'y'
			else:
				new_pattern=new_pattern+'x'
	else:
		new_pattern=pattern
	#count number of x and y's in the pattern
	xcount=0
	ycount=0
	for ch in new_pattern:
		if(ch=='x'):
			xcount=xcount+1
		else:
			ycount=ycount+1
	return findxyvalue(string,xcount,ycount,new_pattern,toggled)
	
def findxyvalue(string,xcount,ycount,new_pattern,toggled):
	#find the maximum possible value of x using (ax+by=len of string)
	xval=int(len(string)/xcount)
	xyval=[]
	if(ycount==0):
		xyval.append([xval,0])
		return checkpatter(string,new_pattern,xcount,ycount,xyval,toggled)
	for i in range(1,xval):
		yval=(len(string)-(i*xcount))/ycount
		if(yval%1==0):
			xyval.append([i,int(yval)])
	return checkpatter(string,new_pattern,xcount,ycount,xyval,toggled)

def checkpatter(string,new_pattern,xcount,ycount,xyval,toggled):
	#check which lenths of x and y match
	
	for xyvalue in xyval:
		output_string=''
		x=string[0:xyvalue[0]]
		y=''
		count=0
		for ch in new_pattern:
			if(ch=='x'):
				count=count+len(x)
			else:
				y=string[count:count+xyvalue[1]]
				break
		for ch in new_pattern:
			if(ch=='x'):
				output_string=output_string+x
			else:
				output_string=output_string+y
		if(string==output_string):
			if(toggled):
				op_arr=[y,x]
				return op_arr
			else:
				op_arr=[x,y]
				return op_arr
	op_arr=[]
	return op_arr

a =patternMatcher("xxyxxy", "gogopowerrangersgogopowerrangers")
print(a)