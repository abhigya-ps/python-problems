def isPalindrome(x):
    rev = str(x)[::-1]
    if str(x) == rev:
        return True
    else:
        return False

print(isPalindrome(121))