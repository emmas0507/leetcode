import numpy as np

def prime_palindrome(N):
    while True:
        if is_prime(N) and is_palindrome(N):
            return N
        else:
            N = N + 1

def is_prime(n):
    n_sqrt = int(np.sqrt(n)) + 1
    for i in range(2, n_sqrt, 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    digit = []
    while n > 0:
        digit = digit + [n % 10]
        n = n // 10
    for i in range(len(digit)//2):
        if digit[i] != digit[len(digit)-1-i]:
            return False
    return True

N = 13
print(prime_palindrome(N))
