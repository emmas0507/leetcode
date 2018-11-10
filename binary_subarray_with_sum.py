def binary_subarray_with_sum(input, target):
    index_dict = {0: [-1]}
    sum = 0
    count = 0
    for i in range(len(input)):
        sum = sum + input[i]
        if sum in index_dict.keys():
            index_dict[sum] = index_dict[sum] + [i]
        else:
            index_dict[sum] = [i]
    for s in range(sum, target-1, -1):
        if s in index_dict.keys() and s - target in index_dict.keys():
            count = count + len(index_dict[s]) * len(index_dict[s-target])
    print(index_dict)
    return count

input = [1,0,1,0,1]
target = 2
print(binary_subarray_with_sum(input, target))
