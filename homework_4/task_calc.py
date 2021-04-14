def calc(fraction):
    result = []
    numerator, denominator = [int(i) for i in fraction.split('/')]
    while denominator > 0:
        q = numerator // denominator
        c = denominator
        denominator = numerator - denominator * q
        numerator = c
        result.append(q)
    return result


