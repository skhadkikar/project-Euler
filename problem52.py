
def check_digits(num):
    digits = set(str(num))
    for x in range(2,7):
        xnum = num * x
        xnum = str(xnum)
        for i in range(xnum.__len__()):
            if xnum[i] not in digits:
                return False
    return True

for x in range(100000,1000000):
    if check_digits(x):
        print(x)