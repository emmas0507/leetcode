def transpose_file(txt):
    txt_array = []
    txt_row = []
    for r in txt:
        if r != ' ' and r != '\n':
            txt_row = txt_row + [r]
        elif r == '\n':
            txt_array = txt_array + [txt_row]
            txt_row = []
    txt_array = txt_array + [txt_row]
    print(txt_array)
    txt_tran = ''
    for j in range(len(txt_array[0])):
        for i in range(len(txt_array)):
            txt_tran = txt_tran + ' ' + txt_array[i][j]
        txt_tran = txt_tran + '\n'

    return txt_tran[:(-1)]

txt = "a b \n c d"
print(transpose_file(txt))
