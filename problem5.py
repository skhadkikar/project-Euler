# mult = 1
# for x in range(1,21):
#     mult *= x
# print(mult)

# 2, 3, 5, 7, 11, 13, 17, 19

# primes = [2, 3, 5, 7, 11, 13, 17, 19]
# mult = 1
# for x in range(primes.__len__()):
#     mult *= primes[x]
# print(mult)

primes = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19] # union of set of all prime factors of numbers 2 through 20
mult = 1
for x in range(primes.__len__()):
    mult *= primes[x]
print(mult)