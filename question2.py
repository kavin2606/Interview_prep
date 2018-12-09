import numpy as np
ip_list=[int(x) for x in input().split()]
ip_list=np.asfarray(ip_list)

def listmul(ip_list):
	op_list=[]
	for i in range(0,len(ip_list)):
		temp=1
		for j in range(0,len(ip_list)):
			if i!=j:
				temp=temp*ip_list[j]
		op_list.append(temp)
	return op_list

op_list = listmul(ip_list)
print(op_list)