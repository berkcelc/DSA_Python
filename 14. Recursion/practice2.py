# Calculate the power of number using recursion

def get_power(num, n):
    assert int(n) == n, 'We accept only integers'
    if n == 0:
        return 1
    if n == 1:
        return num
    else:
        return num * get_power(num ,(n-1))
    
get_power(5,3)