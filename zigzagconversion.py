def zigzagconversion(input, nrow):
    if len(input) <= nrow:
        res = [None] * nrow
        for i in range(len(input)):
            res[i] = input[i]
        return [res]
    # if len(input) < 2 * nrow - 1:
    res = [[i for i in input[0:nrow]]]
    j = nrow
    i = nrow - 2
    while i > 0 and j < len(input):
        tmp = [None] * nrow
        tmp[i] = input[j]
        j = j + 1
        i = i - 1
        res = res + [tmp]
    if j < len(input):
        res = res + zigzagconversion(input[j:], nrow)
    return res

def print_zigzag(res):
    for i in range(len(res[0])):
        for j in range(len(res)):
            if res[j][i] is not None:
                print(res[j][i])

input = 'PAYPALISHIRING'
nrow = 3
print_zigzag(zigzagconversion(input, nrow))
