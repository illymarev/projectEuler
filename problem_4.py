outputs = []
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        output = str(i * j)
        if output == output[::-1]:
            outputs.append(int(output))
            break
print(max(outputs))
