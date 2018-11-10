def binary_trees_with_factors(input):
    input = sorted(input)
    fact_dict = {}
    count = {}
    for i in input:
        fact_dict[i] = []
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[i] * input[j] in fact_dict.keys():
                fact_dict[input[i] * input[j]] = fact_dict[input[i] * input[j]] + [(input[i], input[j])]
    for i in range(len(input)):
        if len(fact_dict[input[i]]) == 0:
            count[input[i]] = 1
        else:
            count[input[i]] = 1
            for (f1, f2) in fact_dict[input[i]]:
                if f1 == f2:
                    count[input[i]] = count[input[i]] + count[f1] * count[f2]
                else:
                    count[input[i]] = count[input[i]] + count[f1] * count[f2] * 2
    print(count)
    return sum(count.values())

input = [2, 4, 5, 10, 16]
input = [2, 3, 4, 6, 12]
binary_trees_with_factors(input)
