def in_array(array1, array2):
    
    r = []
    
    for sub_string in array1:
        for string in array2:
            if sub_string in string:
                r.append(sub_string)
            else:
                continue

    return sorted(set(r))
