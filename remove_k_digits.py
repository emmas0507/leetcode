def remove_k_digits(input, K):
    if K == 0:
        return input
    if int(input[1]) == 0:
        i = 2
        while int(input[i]) == 0:
            i = i + 1
        return remove_k_digits(input[i:], K-1)
    else:
        for i in range(len(input)-1):
            if int(input[i]) > int(input[i+1]):
                new_input = input[:i] + input[(i+1):]
                return remove_k_digits(new_input, K-1)
        return remove_k_digits(input[:(-1)], K-1)

input = '1020001'
K = 2
print(remove_k_digits(input, K))
