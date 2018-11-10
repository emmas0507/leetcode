import math
def func(n, k):
    seq = range(1, n+1)
    k = k - 1
    def permutation_sequence(seq, k):
        print('seq is{}, k is {}'.format(seq, k))
        if len(seq) == 1:
            return [seq[0]]
        else:
            val_index = k / math.factorial(len(seq)-1)
            val = seq[val_index]
            seq = [seq[i] for i in range(len(seq)) if i != val_index]
            k = k - val_index * math.factorial(len(seq))
            return [val] + permutation_sequence(seq, k)
    return permutation_sequence(seq, k)

n = 4
k = 17
print(func(n, k))
