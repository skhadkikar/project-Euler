

def isPalindrome(num):
    number = num
    reverse = 0
    # print(num)
    while (number > 0):
        # print(number, reverse)
        digit = number % 10
        reverse *= 10
        reverse += digit
        number = number // 10
    if num == reverse: 
        # print(num)
        return True
    else: 
        return False

lst = []
for x in range(999,101,-1):
    for y in range(999,x-1,-1):
        pally = x*y
        # print(x,y,pally)
        if isPalindrome(pally):
            lst.append(pally)
lst.sort()
print(lst.pop())
