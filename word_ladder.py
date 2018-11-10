def word_ladder(beginword, endword, wordlist):
    char_list = [chr(ord('a')+i) for i in range(26)]
    word_dict = {}
    for w in wordlist:
        word_dict[w] = 1
    wordstack = [beginword]
    visited_dict = {beginword: 1}
    step = 1
    while len(wordstack) > 0:
        tmp_wordstack = []
        for w in wordstack:
            if w == endword:
                return step
            for i in range(len(w)):
                for c in char_list:
                    new_w = w[0:i] + c + w[(i+1):]
                    if new_w != w and new_w in word_dict.keys() and new_w not in visited_dict.keys():
                        print('added new word {}'.format(new_w))
                        tmp_wordstack = tmp_wordstack + [new_w]
                        visited_dict[new_w] = 1
        wordstack = tmp_wordstack
        step = step + 1
        print('wordstack and step are {}, {}'.format(wordstack, step))
    return 0

beginword = 'hit'
endword = 'cog'
wordlist = ["hot","dot","dog","lot","log"]

print(word_ladder(beginword, endword, wordlist))
