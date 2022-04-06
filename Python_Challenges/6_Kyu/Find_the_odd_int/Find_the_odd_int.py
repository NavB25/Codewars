def find_it(seq):
    for num in seq:
        occ = seq.count(num)
        if occ % 2 != 0:
            return num
        else:
            continue
