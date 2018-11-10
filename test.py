def input(x, y):
    def helper(y):
        x[0] = y
    helper(y)
    print(x)
    return x

x = [2,2]
y = 1
print(input(x, y))
