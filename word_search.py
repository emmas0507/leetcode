def word_search(board, target):
    def helper(board, i, j, visited, target):
        print('board char is {}'.format(board[i][j]))
        if len(target) == 0:
            return True
        res = False
        if i > 0 and board[i-1][j] == target[0] and ~visited[i-1][j]:
            visited[i-1][j] = True
            if helper(board, i-1, j, visited, target[1:]):
                res = True
        if i < len(board)-1 and board[i+1][j] == target[0] and ~visited[i+1][j]:
            visited[i+1][j] = True
            if helper(board, i+1, j, visited, target[1:]):
                res = True
        if j > 0 and board[i][j-1] == target[0] and ~visited[i][j-1]:
            visited[i][j-1] = True
            if helper(board, i, j-1, visited, target[1:]):
                res = True
        if j < len(board[0])-1 and board[i][j+1] == target[0] and ~visited[i][j+1]:
            visited[i][j+1] = True
            if helper(board, i, j+1, visited, target[1:]):
                res = True
        return res
    # visited = [[False] * len(target[0]) for i in range(len(target))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == target[0]:
                visited = [[False] * len(board[0]) for k in range(len(board))]
                visited[i][j] = True
                # import pdb; pdb.set_trace()
                res = helper(board, i, j, visited, target[1:])
                if res:
                    return True
                else:
                    continue
    return False

board =[['A','B','C','E'], ['S','F','C','S'],['A','D','E','E']]
target = 'ABCCED'
target = 'SEE'
print(word_search(board, target))
