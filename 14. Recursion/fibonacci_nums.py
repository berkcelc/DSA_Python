

# factorial numbers


def factorial_num(num):

    assert int(num) == num and num >= 0, "The input has to be positive integer"

    if num in [0,1]:
        return num
    else:
        num = factorial_num(num - 1) + factorial_num(num - 2)
        return num 
        

factorial_num(10)