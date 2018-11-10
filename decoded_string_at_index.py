def decoded_string_at_index(S, K):
    char_str = S[0]
    string_list = []
    rep_list = []

    for i in range(1, len(S)):
        if S[i-1].isalpha() and S[i].isalpha():
            char_str = char_str + S[i]
        elif S[i-1].isalpha() and S[i].isdigit():
            number = S[i]
        elif S[i-1].isdigit() and S[i].isdigit():
            number = number + S[i]
        elif S[i-1].isdigit() and S[i].isalpha():
            n = int(number)
            rep_list = rep_list + [n]
            string_list = string_list + [char_str]
            char_str = S[i]
            number = ''

    n = int(number)
    rep_list = rep_list + [n]
    string_list = string_list + [char_str]
    string_len = [len(string_list[0])]
    for i in range(1, len(rep_list)):
        string_len = string_len + [string_len[i-1] * rep_list[i-1] + len(string_list[i])]
    print('string_list and rep_list are {}, {}'.format(string_list, rep_list))
    print('string_len is {}'.format(string_len))

    for i in range(len(string_len)-1, 0, -1):
        K = K % string_len[i]
        print('i is {}, K is {}'.format(i, K))
        if K > string_len[i-1] * rep_list[i-1]:
            return string_list[i][K - string_len[i-1] * rep_list[i-1] - 1]
    return string_list[0][(K-1) % string_len[0]]



# S = "leet2code3"
S = "abf2cd3"
K = 10

print(decoded_string_at_index(S,K))
