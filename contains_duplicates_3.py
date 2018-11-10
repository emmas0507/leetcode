def contains_duplicates_3(input, k, t):
    for i in range(len(input)-k):
        end_index = min(i+k+1, len(input))
        for j in range(i+1, end_index):
            if abs(input[i] - input[j]) <= t:
                return True
    return False

def contains_duplicates_3(input, k, t):
    i = 1
    j = 0
    valid_number = [input[0]]
    while i < len(input):
        if i - j > k:
            j = j + 1
            valid_number = valid_number[1:]
        print(valid_number)
        for n in range(input[i]-t, input[i]+t+1):
            if n in valid_number:
                return True
        valid_number = valid_number + [input[i]]
        i = i + 1
    return False

# input = [1,2,3,1]
# k = 3
# t = 0
input = [1,0,1,1]
k = 1
t = 2
input = [1,5,9,1,5,5]
k = 2
t = 3
print(contains_duplicates_3(input, k, t))
