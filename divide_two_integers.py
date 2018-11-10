def divide_two_integers(dividend, divisor):
    val = 0
    if divisor < 0:
        while abs(dividend) > abs(divisor):
            val = val - 1
            dividend = dividend + divisor
    else:
        while abs(dividend) > abs(divisor):
            val = val + 1
            dividend = dividend - divisor
    return val

dividend = 7
divisor = -3
print(divide_two_integers(dividend, divisor))
