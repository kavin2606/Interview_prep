stepInc = [int(x) for x in input().split()]
totSteps = int(input())

def NoOfWays(n,xarr):
	if(n<0):
		return 0
	if(n==1):
		return 1
	else:
		return sum(NoOfWays(n-x, xarr) for x in xarr)

totalWays = NoOfWays(totSteps,stepInc)
print(totalWays) 