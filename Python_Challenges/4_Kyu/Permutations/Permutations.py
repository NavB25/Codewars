def permutations(string):
    
    import itertools
    lst = [x for x in string]
    return list(set([''.join(x) for x in itertools.permutations(lst)]))
