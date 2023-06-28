


def factorial(y):
    if y <= 1:
        return 1
    else:
        return y * factorial(y-1)


def sum(n):

    if n > 1:
        n = factorial(n)

    if n <= 0:
        return 0
    else:
        return n + sum(n-1)


sum(3)