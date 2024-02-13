def isPalindrome(v):
	rev = ''.join(reversed(v))

	if (v == rev):
		return True
	return False


v = "ama"
ans = isPalindrome(v)

if (ans):
	print("Yes")
else:
	print("No")
