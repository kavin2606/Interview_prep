def is_palindrome(str):
	return (str == str[::-1])

def make_palindrome(string):

	if(is_palindrome(string)):
		return string

	if string[0] == string[-1]:
		return string[0] + make_palindrome(string[1:-1]) + string[-1]
	else:
	
		one = string[0] + make_palindrome(string[1:]) + string[0]
		two = string[-1] + make_palindrome(string[:-1]) + string[-1]

		if len(one) < len(two):
			return one
		elif len(two) < len(one):
			return two
		else:
			return min(one,two)

a = make_palindrome("race")
print(a)