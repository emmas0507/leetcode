def summary_ranges(input):
    l = 0
    result = []
    for i in input:
        if i == l + 1:
            result = result + [str(i-1)]
        elif i > l + 1:
            result = result + ["{}->{}".format(l, (i-1))]
        l = i + 1
    if l < 99:
        result = result + ["{}->{}".format(l, 99)]
    elif l == 99:
        result = result + ["{}".format(99)]
    return result

input = [0, 1, 3, 50, 75]
print(summary_ranges(input))


