import numpy as np
ip_data=open("/Users/kavinarasu/Documents/GIT REPOS/Interview_prep/hosts_access_log_00.txt","r")
ip_data= ip_data.read().splitlines()
ip_data= [x.split() for x in ip_data]
host=[]

def write_func(ip_data):
	for x,xi in enumerate(ip_data):
		host.append(xi[0])
	new_dict=dict()
	for i in host:
		if(new_dict.get(i)==None):
			new_dict[i]=1
		else:
			temp=new_dict.get(i)
			new_dict[i]=temp+1
	ip_file_name="hosts_access_log_00.txt"
	op_file_name="/Users/kavinarasu/Documents/GIT REPOS/Interview_prep/record_"+ip_file_name
	op_data=open(op_file_name,"w")

	for key,values in new_dict.items():
		#print(key,values)
		op_data.write("%s %i\n" % (key, values))

	op_data.close()	


write_func(ip_data)
