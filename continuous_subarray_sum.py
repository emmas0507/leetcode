def continuous_subarray_sum(input, K):
    index_dict = {}
    sum = 0
    for i in range(len(input)):
        sum = (sum + input[i]) % K
        print('i is {} and sum is {}'.format(i, sum))
        if i > 0 and sum == 0:
            return input[:(i+1)]
        if sum in index_dict.keys() and (i - index_dict[sum]) > 1:
            return input[(index_dict[sum]+1):(i+1)]
        else:
            index_dict[sum] = i
    return None

# input = [23, 2, 4, 6, 7]
input = [23, 2, 6, 4, 7]
K = 6

print(continuous_subarray_sum(input, K))
