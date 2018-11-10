def next_permutation(input):
    i = len(input) - 1
    while i >= 0:
        if input[i-1] < input[i]:
            break
        else:
            i = i - 1
    if i == 1 and input[0] > input[1]:
        return sorted(input)
    pivot = input[i-1]
    print('pivot is {}'.format(pivot))
    replace = 100000
    replace_index = None
    for j in range(i, len(input)):
        if input[j] > pivot and input[j] <= replace:
            replace = input[j]
            replace_index = j
    tmp = input[i-1]
    input[i-1] = input[replace_index]
    input[replace_index] = tmp
    return input[:i] + sorted(input[i:])

input = [1, 2, 7, 4, 3, 1]
print(next_permutation(input))
