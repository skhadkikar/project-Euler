import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

def power_trunc(num, exp, dig=10):
    lim = 10**dig
    trunc = num%lim
    if exp == 0:
        return 1
    elif exp == 1:
        return trunc
    elif exp == 2:
        return (trunc**2)%lim
    elif exp < 0:
        return 0
    rec = power_trunc(num,exp-1,dig)
    rec = rec * trunc
    rec = rec % lim
    return rec

def self_power_series(max,dig=10):
    pows = list()
    for i in range(1,max+1):
        self_power = power_trunc(i,i,dig)
        pows.append(self_power)
        print(i,self_power)
    sum = 0
    for i in pows:
        sum += i
    return sum

ans = self_power_series(1000)
ans = ans % 10**10
print(ans)

sys.setrecursionlimit(1000)
