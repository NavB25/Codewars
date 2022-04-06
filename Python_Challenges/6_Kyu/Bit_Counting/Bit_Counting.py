def count_bits(n):
    from collections import Counter
    return Counter(bin(n))['1']
