def find132pattern(input):
    third = -10000
    s = []
    for i in range(len(input)-1, -1, -1):
        if input[i] < third:
            return True
        else:
            while (len(s) > 0) and (input[i] > s[-1]):
                third = s[-1]
                s = s[:(-1)]
        s = s + [input[i]]
        print('i is {}, third is {}. s is {}'.format(i, third, s))
    return False

input = [1,2,3,4]
input = [4,3,2,1]
input = [3,1,2,4]
input = [-1, 3, 2, 0]
print(find132pattern(input))
