import math

lim = 10**10
num = 1
for _ in range(7830457):
    num *= 2
    num %= lim
num *= 28433
num %= lim
num += 1
print(num)