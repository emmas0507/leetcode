def out_of_boundary_path(m, n, pos, N):
    [i, j] = pos
    count = 0
    path = [(i, j)]
    for k in range(N):
        tmp = []
        for (i, j) in path:
            if i == 0:
                count = count + 1
                print('k is {}, i,j are {}, {}'.format(k, i, j))
            if i == (m-1):
                count = count + 1
            if j == 0:
                count = count + 1
            if j == (n-1):
                count = count + 1
            if i != 0:
                tmp = tmp + [(i-1, j)]
            if i != (m-1):
                tmp = tmp + [(i+1, j)]
            if j != 0:
                tmp = tmp + [(i, j-1)]
            if j != (n-1):
                tmp = tmp + [(i, j+1)]
        path = tmp
    return count

m = 1
n = 3
N = 3
pos = (0, 1)
print(out_of_boundary_path(m, n, pos, N))
