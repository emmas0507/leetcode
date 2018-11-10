def range_sum_query(input, target):
    input_sum = [[0] * len(input[0]) for i in range(len(input))]
    sum = 0
    input_dict = {}
    for i in range(len(input)):
        for j in range(len(input[0])):
            sum = sum + input[i][j]
            if sum in input_dict.keys():
                input_dict[sum] = input_dict[sum] + [(i, j)]
            else:
                input_dict[sum] = [(i, j)]
    for s in input_dict.keys():
        (start_i, start_j) = input_dict[s][0]
        if s + target in input_dict.keys():
            for (i, j) in input_dict[s+target]:
                if i >= start_i and j >= start_j:
                    return [(start_i, start_j), (i, j)]
    return None

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]

target = 8

print(range_sum_query(matrix, target))
