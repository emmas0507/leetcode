def integer_replacement(input):
    q = [input]
    steps = 0
    while True:
        tmp = []
        for n in q:
            if n == 1:
                return steps
            elif n % 2 == 1:
                tmp = tmp + [n+1, n-1]
            else:
                tmp = tmp + [n/2]
        q = tmp
        steps = steps + 1

print(integer_replacement(7))
