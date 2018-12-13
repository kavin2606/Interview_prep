def longestPalindromicSubstring(string):
	prevstr=""
	newstr=""

	for i in range(len(string)):
		for j in reversed(range(len(string))):
			if(string[i]==string[j]):
				newstr=get_pal_len(string[i:j+1])
			if(len(newstr)>len(prevstr)):
				prevstr=newstr
	return prevstr

def get_pal_len(string):
	rev=""
	for k in reversed(range(len(string))):
		rev=rev+string[k]
	if(string==rev):
		return string
	else:
		return ""
b = "abaxyzzyxf"
a = longestPalindromicSubstring(b)
print(b,a)