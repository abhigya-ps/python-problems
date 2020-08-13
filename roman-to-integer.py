def romanToInt(s):
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0

    for i in range(len(s)):
        letter = s[i]
        prevLetter = s[i-1]
        current  = dict[letter]
        
        if i == 0:
            prevLetter = None
        
        if letter == 'V' and prevLetter == 'I':
                num += 5 - 1 - 1
                continue
        if letter == 'X' and prevLetter == 'I':
                num += 10 - 1 - 1
                continue
        if letter == 'L' and prevLetter == 'X':
                num += 50 - 10 - 10
                continue
        if letter == 'C' and prevLetter == 'X':
                num += 100 - 10 - 10
                continue
        if letter == 'D' and prevLetter == 'C':
                num += 500 - 100 - 100
                continue
        if letter == 'M' and prevLetter == 'C':
                num += 1000 - 100 - 100
                continue

        num += current
    
    return num

print(romanToInt('MMMCDXC'))