def delete_nth(order,max_e):
    
    new_lst = []
    
    for num in order:
        
        if new_lst.count(num) < max_e:
            new_lst.append(num)
        
    return new_lst
