total = 0

i = 3
while i < 1000:
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
    i += 1

print(total)