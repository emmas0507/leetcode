def sum_of_subarray_minimum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        N = len(alist)
        min_value = min(alist)
        min_index = alist.index(min_value) + 1
        if min_index == 1:
            sum_ = sum_of_subarray_minimum(alist[1:]) + min_value * min_index * (N+1-min_index)
        elif min_index == N:
            sum_ = sum_of_subarray_minimum(alist[:(-1)]) + min_index * (N+1-min_index)
        else:
            sum_ = sum_of_subarray_minimum(alist[:(min_index-1)]) + sum_of_subarray_minimum(alist[min_index:]) + min_index * (N+1-min_index)
        print('alist is {} and sum_ is {}'.format(alist, sum_))
        return sum_

alist = [3,1,2,4]
print(sum_of_subarray_minimum(alist))
