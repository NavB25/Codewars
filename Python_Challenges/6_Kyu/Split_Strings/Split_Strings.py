def solution(s):
    lst = []
    n = 2
    
    #even number of characters
    if len(s) % 2 == 0:
        for i in range(0,len(s),n):
            lst.append(s[i:i+n])
  
    #odd number of characters
    else:
        s += '_'
        for i in range(0,len(s),n):
            lst.append(s[i:i+n])
    
    return lst
