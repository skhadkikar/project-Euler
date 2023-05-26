i = 1
j = 2
k = 0

#def fibonacci(i,j):
#    k = i + j
#    print("k --> ", k)
#    i = j
#    print("i --> ", i)
#    j = k
#    print("j --> ", j)

total = 0

while i + j <= 4000000:
#    fibonacci(i,j)
    k = i + j
    print("k --> ", k)
    i = j
    print("i --> ", i)
    j = k
    print("j --> ", j)
    
    if k % 2 == 0:
        total += k

print(total + 2)


