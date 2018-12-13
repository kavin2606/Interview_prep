def longestSubstringWithoutDuplication(string):
	prev_max=""
	curr_max=""
	my_dic={}
	for i,ch in enumerate(string):
		if((ch in my_dic) and (my_dic[ch]>=my_dic[curr_max[0]])):
			temp=curr_max
			curr_max=string[(my_dic[ch]+1):i+1]
			my_dic[ch]=i
			if(len(temp)>len(prev_max)):
				prev_max=temp
		else:
			my_dic[ch]=i
			curr_max=curr_max+ch
	if(len(curr_max)>=len(prev_max)):
		prev_max=curr_max
	return prev_max

string=input()
print(string,longestSubstringWithoutDuplication(string))