def plusOne(digits):
    

    if digits == [9]:
        digits[0] = 1
        digits.append(0)
        return digits

    digits[-1] = digits[-1] + 1
    allNine = True

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] - 1 != 9:
            allNine = False
        if digits[i] > 9 and len(digits) > 1:
            digits[i] = digits[i] - 10
            digits[i-1] += 1

    if allNine == True:
        digits[0] = 1
        digits[-1] = digits[-1] - 1
        digits.append(0)
    return digits

print(plusOne([1,2,3,4,5]))
print(plusOne([9,9,9,9,9]))