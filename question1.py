ip_list=[int(x) for x in input().split()]
k=int(input())

def check_sum(ip_list, k):
	l=set()
	for i in ip_list:
		if k-i in l:
			return True
		else:
			l.add(i)
	return False

a = check_sum(ip_list, k)

print(a)
