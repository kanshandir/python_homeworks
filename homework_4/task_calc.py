def calc(fraction):
    result = []
    numerator, denominator = [int(i) for i in fraction.split('/')]
    while denominator > 0:
        q = numerator // denominator
        numerator, denominator = denominator, numerator % denominator
        result.append(q)
    return result


