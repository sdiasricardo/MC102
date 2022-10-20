a = [9, 7, 3, 5, 10, 21, 4, 1]


for k in range(len(a) - 1):
    for i in range(len(a) - 1, k, -1):
        if a[i - 1] > a[i]:
            aux = a[i]
            a[i] = a[i - 1]
            a[i - 1] = aux

print(a)