
def replacement_primes(num):
    replacements = []
    num = str(num)
    for i in range(0,num.__len__()-1):
        for j in range(i+1,num.__len__()-1):
            rep = num[:i] + '*' + num[i+1:j] + '*' + num[j+1:]
            replacements.append(rep)
    for i in range(0,num.__len__()-1):
        for j in range(i+1,num.__len__()-1):
            for k in range(j+1,num.__len__()-1):
                rep = num[:i] + '*' + num[i+1:j] + '*' + num[j+1:k] + '*' + num[k+1:]
                replacements.append(rep)
    for i in range(0,num.__len__()-1):
        for j in range(i+1,num.__len__()-1):
            for k in range(j+1,num.__len__()-1):
                for l in range(k+1,num.__len__()-1):
                    rep = num[:i] + '*' + num[i+1:j] + '*' + num[j+1:k] + '*' + num[k+1:l] + '*' + num[l+1:]
                    replacements.append(rep)
    return replacements

# thing = replacement_primes(56003)
# for i in thing:
#     print(i)

primes = [2]
for i in range(3,1000000,2):
    prime = True
    for j in range(primes.__len__()):
        if i % primes[j] == 0: # if i is divisible by a prime, then it is composite
            prime = False
            break
    if prime:
        # print(i)
        primes.append(i)

# primes.sort()
primes = [x for x in primes if x > 100000]
print('preprocessing done')

checked = set()
for prime in primes:
    if prime > 100000:
        # print(prime)
        replacements = replacement_primes(prime)
        for rep in replacements:
            # print(rep)
            if rep not in checked:
                checked.add(rep)
                count = 0
                for i in range(10):
                    num = int(rep.replace('*',str(i)))
                    # print(num)
                    if primes.__contains__(num):
                        count += 1
                if count >= 8: 
                    print(prime) 
                    print(rep)
                # print()
    # break