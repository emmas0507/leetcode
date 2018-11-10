def decode_ways(alist):
    if len(alist) == 0:
        return 1
    if len(alist) == 1:
        return 1
    elif int(alist[-2]) == 1:
        return decode_ways(alist[:(-2)]) + decode_ways(alist[:(-1)])
    elif int(alist[-2]) == 2 and int(alist[-1]) <= 6:
        return decode_ways(alist[:(-2)]) + decode_ways(alist[:(-1)])
    else:
        return decode_ways(alist[:(-1)])

a = "221"
print(decode_ways(a))
