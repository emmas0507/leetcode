def maximum_product_subarray(input):
    max_i = [input[0]] * len(input)
    min_i = [input[0]] * len(input)
    for i in range(1, len(input)):
        max_i[i] = max(max(max_i[i-1]*input[i], min_i[i-1]*input[i]), input[i])
        min_i[i] = min(min(max_i[i-1]*input[i], min_i[i-1]*input[i]), input[i])
    return max(max_i)

input = [-2,0,-1]
print(maximum_product_subarray(input))
