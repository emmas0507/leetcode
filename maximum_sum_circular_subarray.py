def maximum_sum_circular_subarray(array):
    max1 = -100000
    currsum = 0
    for i in array:
        if currsum >= 0:
            currsum = currsum + i
        else:
            currsum = i
        if currsum > max1:
            max1 = currsum
    min1 = 100000
    currsum = 0
    for i in array:
        if currsum <= 0:
            currsum = currsum + i
        else:
            currsum = i
        if currsum < min1:
            min1 = currsum
    max2 = sum(array) - min1
    return max(max1, max2)

array = [1,-2,3,-2]
array = [5, -3, 5]
array = [3, -1, 2, -1]
print(maximum_sum_circular_subarray(array))

