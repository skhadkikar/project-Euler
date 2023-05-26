import math

def n_choose_r(n,r):
    r_fac = fac(r)
    nr_fac = fac(n-r,r,r_fac)
    n_fac = fac(n,n-r,nr_fac)
    return n_fac / (r_fac * nr_fac)

def fac(num, small=1, init=1):
    if num == small:
        return num * init
    return fac(num-1) * num

total = 0
for n in range(1,101):
    for r in range(1,n//2+1):
        if n_choose_r(n,r) > 1000000:
            # print(f"n:{n}\tr:{r}")
            count = (2 * (n//2 - r + 1))
            if not n%2: count -= 1
            total += count
            break
print(total)