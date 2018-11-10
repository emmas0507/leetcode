def mini_parser(input):
    if input[0] != '[':
        return input
    s = []
    val = ''
    for i in range(len(input)):
        curr = input[i]
        if curr.isdigit():
            val = val + curr
        else:
            val = ''
        if curr.isdigit() and i != len(input)-1 and (not input[i+1].isdigit()):
            s = s + [int(val)]
        if curr == '[':
            s = s + [curr]
        elif curr == ']':
            new_list = []
            for k in range(len(s)-1,-1,-1):
                new_item = s[k]
                if new_item == '[':
                    break
                else:
                    new_list = [new_item] + new_list
            s = s[:k] + [new_list]
        print('i is {}, val is {}, s is {}'.format(i, val, s))
    return s[0]

input = '[1,[2,3,[5,[6]]]]'
print(mini_parser(input))
