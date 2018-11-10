def get_abbreviation(word):
    if len(word) <= 2:
        return word
    else:
        return word[0] + str(len(word)-2) + word[-1]


def unique_abbreviation(word_list, target_w):
    abb_dict = {}
    for w in word_list:
        abb_w = get_abbreviation(w)
        if abb_w in abb_dict.keys():
            abb_dict[abb_w] = abb_dict[abb_w] + [w]
        else:
            abb_dict[abb_w] = [w]

    abb_target = get_abbreviation(target_w)
    if abb_target not in abb_dict.keys():
        return True
    else:
        word_list = abb_dict[abb_target]
        for w in word_list:
            if w != target_w:
                return False
        return True

word_list = ['dear', 'door']
target_w = 'door'
print(unique_abbreviation(word_list, target_w))
