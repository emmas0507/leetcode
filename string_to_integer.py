def string_to_integer(str):
    number = ''
    for i in range(len(str)):
        if str[i] != ' ':
            break
    if str[i] == '+' or str[i] == '-' or (ord(str[i]) >= ord('1') and ord(str[i]) <= ord('9')):
        number = number + str[i]
        i = i+1
        while i<len(str) and ord(str[i]) >= ord('1') and ord(str[i]) <= ord('9'):
            number = number + str[i]
            i = i + 1
        if int(number) > pow(2, 31):
            return pow(2, 31)
        elif int(number) < -pow(2, 31):
            return -pow(2, 31)
        else:
            return number
    else:
        return None

str = '42'
str = '  -42'
str = "4193 with words"
str = "words and 987"
str = "-91283472332"
print(string_to_integer(str))
