import math

# facs = list()
# for i in range(11):
#     facs.append(math.factorial(i))

# with open('digit_factorial_chains.txt','w') as f:
#     for i in range(10**7):
#         sum = 0
#         num = i
#         while num >= 10:
#             dig = num % 10
#             num //= 10
#             sum += facs[dig]
#         sum += facs[num]
#         f.write(str(sum) + '\n')

chains = []
with open('digit_factorial_chains.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        chains.append(int(line.rstrip()))
print('preprocessing done')

lengths = []
for i in range(1000000):
    count = 1
    point = i
    while point != chains[point]:
        point = chains[point]
        count += 1
        if point in [169,363601,1454]:
            count += 2
            break
        elif point in [871,45361]:
            count += 1
            break
        elif point in [872,45362]:
            count += 1
            break
    lengths.append(count)

print(lengths.count(60))