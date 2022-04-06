def increment_string(strng):
    import re
    position = 0
    lst = []
    
    if strng == "" or strng[-1].isdigit() == False:
        return strng + '1'

    else:
        for x,y in enumerate(strng[::-1]):
            if y.isdigit():
                lst.append(y)
            else:
                position = x
                break
        
        new_lst = list(reversed((strng[-position-1::-1])))
        n = len(lst)
        fst = ''.join(lst[::-1])
        second = ''.join(new_lst)
        total = int(fst) + 1
        
        if second.isdigit():
            return str(total).zfill(n)
        else:
            return second + str(total).zfill(n)
