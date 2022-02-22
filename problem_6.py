num_squares = []
for i in range(101):
    num_squares.append(i)
print(sum(num_squares) * sum(num_squares) - sum(map(lambda x: x * x, num_squares)))
