n1, n2 = 0, 1
nth = 0
even_fib_numbers = []
while nth < 4000000:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    even_fib_numbers.append(nth) if nth % 2 == 0 else None
print(sum(even_fib_numbers))
