def longest_substring_without_repeating_char(string):
    left = 0
    max_len = 0
    char_dict = {}
    for i in range(len(string)):
        s = string[i]
        if s in char_dict.keys():
            left = char_dict[s] + 1
        char_dict[s] = i
        curr_len = (i - left) + 1
        if max_len < curr_len:
            max_len = curr_len
        print('i is {}, curr_len is {}, max_len is {}'.format(i, curr_len, max_len))
    return max_len

string = 'abcabcbb'
print(longest_substring_without_repeating_char(string))
