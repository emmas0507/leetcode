def sum3(input_list):
    input_list = sorted(input_list)
    result_list = []
    for i in range(len(input_list)-3):
        if input_list[i] > 0:
            break
        if input_list[i] == input_list[i-1]:
            continue
        j = i + 1
        k = len(input_list) - 1
        while j < k:
            if input_list[j] + input_list[k] < - input_list[i]:
                j = j + 1
            elif input_list[j] + input_list[k] > - input_list[i]:
                k = k - 1
            else:
                result_list = result_list + [(input_list[i], input_list[j], input_list[k])]
                while (j < k) and (input_list[j] == input_list[j+1]):
                    j = j + 1
                while (j < k) and (input_list[k] == input_list[k-1]):
                    k = k - 1
                j = j + 1
                k = k - 1
    return result_list

input_list = [-1, 0, 1, 2, -1, -4]
print(sum3(input_list))
