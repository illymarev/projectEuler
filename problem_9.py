def find_numbers():
    for c in range(300, 500):
        for b in range(200, 400):
            for a in range(100, 250):
                if a < b < c:
                    if (a ** 2 + b ** 2) == c ** 2:
                        if a + b + c == 1000:
                            print(a, b, c)
                            print(a * b * c)
                            return


find_numbers()
print('Done')
