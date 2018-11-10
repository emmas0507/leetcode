def wiggle_sort_2(input):
    input_len = len(input)
    input = sorted(input)
    mid = input_len // 2
    for i in range(mid):
        tmp = input[i]
        input[i] = input[input_len-i-1]
        input[input_len-i-1] = tmp
    print(input)
    for i in range(0, input_len-1, 2):
        tmp = input[i]
        input[i] = input[i+1]
        input[i+1] = tmp

    return input

input = [3, 4, 5, 5, 6]
print(wiggle_sort_2(input))
