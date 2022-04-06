def square_digits(num):
    result = [str(int(x)**2) for x in str(num)]
    return int("".join(result))
