def reverse_words_in_string(str):
    str = str + ' '
    rev_str = ''
    word = ''
    for i in range(len(str)-1):
        if str[i] == ' ' and str[i+1] != ' ':
            word = ''
        elif str[i] != ' ' and str[i+1] == ' ':
            word = word + str[i]
            rev_str = word + ' ' + rev_str
        elif str[i] == ' ' and str[i+1] == ' ':
            continue
        else:
            word = word + str[i]

    # if str[i] == ' ' and str[i-1] != ' ':
    #     word = word + str[i]
    #     rev_str = word + ' ' + rev_str

    return rev_str

str = "  the sky is blue  "
print(reverse_words_in_string(str))
