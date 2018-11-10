def evaluate(input):
    s = []
    for i in input:
        if i.isdigit():
            s = s + [i]
        else:
            y = s[-1]
            x = s[-2]
            new = eval(x+i+y)
            s = s[:(-2)] + [str(new)]
            print(s)
    return s[0]

input = ["2", "1", "+", "3", "*"]
input = ["4", "13", "5", "/", "+"]
print(evaluate(input))
