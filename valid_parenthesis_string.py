def valid_parenthesis_string(input):
    count = 0
    for i in range(len(input)):
        if count < 0:
            return False
        if input[i] == '(' or input[i] == '*':
            count = count + 1
        else:
            count = count - 1

    count = 0
    for i in range(len(input)-1, -1, -1):
        if count < 0:
            return False
        if input[i] == ')' or input[i] == '*':
            count = count + 1
        else:
            count = count - 1
    return True

input = '*('
print(valid_parenthesis_string(input))

