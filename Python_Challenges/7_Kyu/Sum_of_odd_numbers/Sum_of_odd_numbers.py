def row_sum_odd_numbers(n):
    m = n-1
    lst = [x for x in range((n*m)+1,(n+1)*n,2)]
    return sum(lst)
