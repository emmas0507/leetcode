def smallest_range_2(input_list, k):
    input_list = sorted(input_list)
    min_ = min(input_list)
    max_ = max(input_list)
    res = max_ - min_
    for i in range(len(input_list)-1):
        tmp_min = min(A[0] + k, A[i+1] - k)
        tmp_max = max(A[i] + k, A[-1] - k)
        res = min(res, tmp_max - tmp_min)
    return res

A = [0, 10]
k = 2
A = [1,3,6]
k = 3
print(smallest_range_2(A, k))
