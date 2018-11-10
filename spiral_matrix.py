def spiral_matrix(mat):
    q = len(mat)
    if q == 0:
        return None
    p = len(mat[0])
    if p == 0:
        return None
    if q == 1:
        for j in range(p):
            print(mat[0][j])
    # elif q == 2:
    #     for j in range(p):
    #         print(mat[0][j])
    #     for j in range(p-1, -1, -1):
    #         print(mat[1][j])
    elif p == 1:
        for j in range(q):
            print(mat[j][0])
    # elif p == 2:
    #     for j in range(q):
    #         print(mat[j][0])
    #     for j in range(q-1, -1, -1):
    #         print(mat[j][1])
    else:
        for j in range(p):
            print(mat[0][j])
        for i in range(1, q-1):
            print(mat[i][-1])
        for j in range(p-1, -1, -1):
            print(mat[-1][j])
        for i in range(q-2, 0, -1):
            print(mat[i][0])
        new_mat = [[mat[i][j] for j in range(1, p-1)] for i in range(1, q-1)]
        spiral_matrix(new_mat)

mat = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12], [13,14,15,16]]
spiral_matrix(mat)
