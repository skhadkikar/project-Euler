import math
import time

def prime_factorize(num):
	i = 2
	n = round(math.sqrt(num) + 1)
	while i < n: # find out whether num divides i
		if num % i == 0: # if num does divide i
			print(i)
			#print(f"{i}, {num // i}")
			prime_factorize(num // i) # recursion
			return
		#if i % 1000000000 == 0:
		#	print(i)
		i += 1
	print(num)

x = 600851475143 #600851475143123456789123 #13840293480239842032038421341233
tic = time.time()
prime_factorize(x)
toc = time.time()
print(f"{toc - tic} seconds.")

# max value as far as i can tell this works with: 1384029348023984203
# after this, you start getting exp 2 rounding errors
# but only after the first pfac