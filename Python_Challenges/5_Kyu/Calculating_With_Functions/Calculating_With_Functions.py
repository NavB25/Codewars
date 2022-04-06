import operator


#NUMBER FUNCTIONS
def zero(arg='',n=0):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)

    else:
        return n
     
def one(arg='',n=1):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
      
def two(arg='',n=2):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
      
def three(arg='',n=3):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
def four(arg='',n=4):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
def five(arg='',n=5):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
def six(arg='',n=6):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
def seven(arg='',n=7):
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
def eight(arg='',n=8): 
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n

def nine(arg='',n=9): 
    if arg!='':
        
        num = int(arg[-1])
        ops = arg[0:-1]
        ops_dict = {'+':operator.add, "-":operator.sub, "*": operator.mul,"//":operator.floordiv}
        
        return ops_dict[ops](n,num)
    else:
        return n
    
#OPERATOR FUNCTIONS
def plus(n):
    return f'+{n}'
  
def minus(n):
    return f'-{n}'
    
def times(n):
    return f'*{n}'

def divided_by(n):
    return f'//{n}'
