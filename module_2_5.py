def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        get1 = []
        for j in range(m):
            get1.append(value)
        matrix.append(get1)
    return matrix

result1 = get_matrix(2, 2, 10)

print(result1)


