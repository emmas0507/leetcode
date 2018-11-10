def sum2(input_list):
    input_list = sorted(input_list)
    result_list = []
    i = 0
    j = len(input_list) - 1
    while i < j:
        if input_list[i] + input_list[j] < 0:
            i = i + 1
        elif input_list[i] + input_list[j] > 0:
            j = j - 1
        else:
            result_list = result_list + [(input_list[i], input_list[j])]
            if input_list[j-1] == input_list[j]:
                j = j - 1
            else:
                i = i + 1
    return result_list

input_list = [-3, -2, 1, 2, 2, 3, 4]
print(sum2(input_list))
