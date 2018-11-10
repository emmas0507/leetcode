def sort_func(a, b):
    if (a+b) > (b+a):
        return 1
    else:
        return -1

def largest_number(list):
    list = sorted([str(l) for l in list], cmp=sort_func)
    print(list)
    res = ''
    for i in range(len(list)-1, -1, -1):
        res = res + list[i]
    return res

list = [3, 30, 34, 1, 9]
print(largest_number(list))
