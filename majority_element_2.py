def majority_element_2(input):
    candidate = input[0]
    count = 0
    for i in input:
        if i == candidate:
            count = count + 1
        else:
            if count == 0:
                candidate = i
                count = 1
            else:
                count = count - 1
    print(candidate)
    return candidate

input = [1,1,2,3,4]

print(majority_element_2(input))

def majority_element_2(input):
    m1 = input[0]
    m2 = 0
    c1 = 1
    c2 = 0
    for i in range(1, len(input)):
        x = input[i]
        if x == m1:
            c1 = c1 + 1
        elif x == m2:
            c2 = c2 + 1
            c1 = 1
        elif c1 == 0:
            m1 = x
            c1 = 1
        elif c2 == 0:
            m2 = x
            c2 = 1
        else:
            c1 = c1 - 1
            c2 = c2 - 1
    return m1, m2

input = [1,1,2,2,4,5]
print(majority_element_2(input))
