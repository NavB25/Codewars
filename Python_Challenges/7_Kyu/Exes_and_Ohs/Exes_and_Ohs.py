def xo(s):
    x = 0
    o = 0
    
    for letter in s:
        if letter.lower() == 'x':
            x += 1
        elif letter.lower() == 'o':
            o += 1
        else:
            pass
    
    return x == o
