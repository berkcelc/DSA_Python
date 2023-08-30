

def get_sum_digits(num):
    assert num>=0 and int(num) == num, 'The number has to be a positive integer'

    if num // 10 == 0:
        return num % 10
    else :
        return (num % 10 ) + get_sum_digits(num//10)
    

get_sum_digits(2345)