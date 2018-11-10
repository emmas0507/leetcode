def fraction_to_recurring_decimal(n, m):
    pos = 0
    pos_dict = {}
    decimal = []
    while n != 0:
        val = n * 10 // m
        print('n, pos and val are {},{},{}'.format(n, pos, val))
        if n in pos_dict.keys():
            break
        else:
            decimal = decimal + [str(val)]
            pos_dict[n] = pos
        pos = pos+1
        n = n * 10 - val * m
    if n == 0:
        return '0.' + ''.join(decimal)
    rec_pos =  pos_dict[n]
    print(rec_pos)
    decimal_str = '0.' + ''.join(decimal[:(rec_pos)]) + '(' + ''.join(decimal[(rec_pos):]) + ')'
    return decimal_str

n = 1
m = 8
print(fraction_to_recurring_decimal(n, m))
