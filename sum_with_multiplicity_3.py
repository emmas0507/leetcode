def sum_with_multiplicity_3(input, target):
    array = [0] * 100
    count = 0
    for i in input:
        array[i] = array[i] + 1

    for i in range(target+1):
        for j in range(i, target+1):
            k = target - i - j
            if (k < 0) or (k < j) or (k>len(array)):
                continue
            if (array[i] == 0) or (array[j] == 0) or (array[k] == 0):
                continue
            if (i == j and j == k and array[i] >= 3):
                count = count + array[i] * (array[i]-1) * array[i]-2 / 6
            elif (i == j and j != k and array[i] >= 2):
                count = count + array[i] * (array[i] - 1) * array[k] / 2
            elif (i != j and j == k and array[j] >= 2):
                count = count + array[k] * (array[k] - 1) * array[i] / 2
            else:
                count = count + array[i] * array[j] * array[k]

    return count

input = [1,1,2,2,2,2]
target = 5
input = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(sum_with_multiplicity_3(input, target))
