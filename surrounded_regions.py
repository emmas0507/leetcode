def surrounded_regions(regions):
    N = len(regions)
    M = len(regions[0])

    def helper(i_, j_):
        print('i_ and j_ are {},{}'.format(i_, j_))
        regions[i_][j_] = 'S'
        # print('regions are {}'.format(regions))
        if j_ > 0 and regions[i_][j_-1] == 'O':
            helper(i_, j_-1)
        if j_ < M-1 and regions[i_][j_+1] == 'O':
            helper(i_, j_+1)
        if i_ > 0 and regions[i_-1][j_] == 'O':
            helper(i_-1, j_)
        if i_ < N-1 and regions[i_+1][j_] == 'O':
            helper(i_+1, j_)
        return None

    for i in range(N):
        if regions[i][0] == 'O':
            helper(i, 0)
        if regions[i][M-1] == 'O':
            helper(i, M-1)
    for j_ in range(M):
        if regions[0][j_] == 'O':
            helper(0, j_)
        if regions[N-1][j_] == 'O':
            helper(N-1, j_)

    for i in range(N):
        for j in range(M):
            if (i == 0 or i == N-1 or j == 0 or j == M-1):
                if regions[i][j] == 'S':
                    regions[i][j] = 'O'
            else:
                if regions[i][j] == 'O':
                    regions[i][j] = 'X'
                elif regions[i][j] == 'S':
                    regions[i][j] = 'O'
                else:
                    continue


    return regions

regions = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'X', 'O', 'X']]

print(surrounded_regions(regions))
