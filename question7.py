def underscorifySubstring(string, substring):
	a=[]
	for i,ch in enumerate(string):
		if(string[i:i+len(substring)]==substring):
			a.append([i,(i+len(substring)-1)])
	return merge(a,string)

def merge(a,string):
	mlist=[]
	inmerge=False
	start_idx=0
	end_idx=0
	temp_idx=0
	if(len(a)==1):
		mlist=a
	for i in range(len(a)-1):
		if((not(inmerge)) and ((a[i+1][0])>(a[i][1]+1))):
			mlist.append(a[i])
		elif((not(inmerge)) and ((a[i][1]+1)>=a[i+1][0])):
			start_idx=a[i][0]
			temp_idx=a[i+1][1]
			inmerge=True
		elif((inmerge) and ((a[i][1]+1)>=a[i+1][0])):
				temp_idx=a[i+1][1]
		elif((inmerge) and ((a[i][1]+1)<a[i+1][0])):
				end_idx=temp_idx
				mlist.append([start_idx,end_idx])
				inmerge=False
	if(len(a)==2 and not(inmerge)):
		mlist.append(a[1])
	if(inmerge):
		end_idx=temp_idx
		mlist.append([start_idx,end_idx])
		inmerge=False
				
	return print_us(mlist,string)

def print_us(mlist,string):
	count=0
	for i in range(len(mlist)):
		string=string[:mlist[i][0]+count]+'_'+string[mlist[i][0]+count:]
		count=count+1
		string=string[:(mlist[i][1]+count+1)]+'_'+string[(mlist[i][1]+count+1):]
		count=count+1
	return string


string=input()
substring=input()
a = underscorifySubstring(string, substring)
print(a)
a=underscorifySubstring("testthis is a testtest to see if testestest it works", "test")
print(a)