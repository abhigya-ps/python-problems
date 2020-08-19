def lengthOfLastWord(s):
    if len(s) == 0:
            return 0
    n = 0
    s = s.strip(' ')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            return n
        n = n + 1
    return n

print(lengthOfLastWord('a '))