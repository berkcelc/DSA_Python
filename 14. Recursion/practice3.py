def greatest_common_divisor(gn, sn):

    if gn % sn == 0:
        return sn
    else:
        _r = gn % sn
        return greatest_common_divisor(sn, _r)


greatest_common_divisor(48,18)
