def water_and_jug(x, y, z):
    if x < y:
        tmp = x
        x = y
        y = tmp
    while x % y != 0:
        x = x % y
        if x < y:
            tmp = x
            x = y
            y = tmp
    if z % y == 0:
        return True
    else:
        return False

x = 2
y = 6
z = 5
print(water_and_jug(x, y, z))
