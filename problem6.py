sum_square = 0
for x in range (1,101):
    sum_square += x**2

square_sum = 0
for x in range(1,101):
    square_sum += x
square_sum = square_sum**2

print(square_sum, sum_square, square_sum-sum_square)