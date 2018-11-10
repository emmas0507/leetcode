def champagne_tower(poured, query_glass, query_row):
    curr_level = [poured]
    for i in range(1, query_row+1):
        tmp = [0] * (i+1)
        for j in range(len(curr_level)):
            if curr_level[j] > 1:
                tmp[j] = tmp[j] + (curr_level[j] - 1.0) / 2
                tmp[j+1] = tmp[j+1] + (curr_level[j] - 1.0) / 2
        curr_level = tmp
        print('i is {} and curr_level is {}'.format(i, curr_level))
    return curr_level[query_glass]

poured = 5
query_glass = 2
query_row = 2
print(champagne_tower(poured, query_glass, query_row))
