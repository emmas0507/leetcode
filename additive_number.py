def additive_number(input):

    def help(num1, num2, input):
        print('num1 is {}, num2 is {}, input is {}'.format(num1, num2, input))
        sum_ = num1 + num2
        strtt = str(num1) + str(num2) + str(sum_)
        if input == strtt:
            return True
        elif len(input) > len(strtt) and input[:len(strtt)] == strtt:
            input = input[len(str(num1)):]
            num1 = num2
            num2 = sum_
            return help(num1, num2, input)
        else:
            return False

    for i in range(1, len(input)-1):
        for j in range(i+1, len(input)):
            num1 = int(input[:i])
            num2 = int(input[i:j])
            if help(num1, num2, input):
                return True
    return False


input = '112358'
input = "199100199299"
print(additive_number(input))
