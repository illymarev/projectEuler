divided_by = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(2520, 1000000000, 20):
    outputs = [i % j for j in divided_by]
    if max(outputs) == 0:
        print(i)
        break
