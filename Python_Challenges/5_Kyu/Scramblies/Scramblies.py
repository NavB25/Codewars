def scramble(s1, s2):
    
    import re
    
    s1 = "".join(re.findall("[a-zA-Z]",s1.lower()))
    s2 = "".join(re.findall("[a-zA-Z]",s2.lower()))
    unique = set(s2)
    
    lst = [x for x in unique if s1.count(x) >= s2.count(x) and x in s1]

    return sorted(lst) == sorted(unique)
