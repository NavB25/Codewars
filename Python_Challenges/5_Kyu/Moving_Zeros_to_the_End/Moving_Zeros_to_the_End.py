def move_zeros(array):
    
    non_zeroes = [x for x in array if x != 0]
    zeros = [x for x in array if x == 0]

    non_zeroes.extend(zeros)
    return non_zeroes
