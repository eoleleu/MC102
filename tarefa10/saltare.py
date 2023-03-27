def fibonacci(n: int, a = 1, b = 1, c = 1):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    else:
        return fibonacci(n-1, b, c, c + a)


n = int(input())
print(fibonacci(abs(n)))