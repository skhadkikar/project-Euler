import math

def prime_or_not(num):
	i = 2
	n = round(math.sqrt(num) + 1)
	while i < n:
		if num % i == 0:
			print(f"{num} is not prime.")
			return False
		i += 1
	print(f"{num} is prime.")
	return True
	
count = 1
test = 3
while count < 10001:
    if prime_or_not(test): 
        count += 1
    test += 2

print(test-2)