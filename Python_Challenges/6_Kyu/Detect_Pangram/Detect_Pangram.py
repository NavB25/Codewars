import string as s

def is_pangram(string):
    
    lst = set([x for x in string.lower() if x.isalpha()])
    
    return "".join(sorted(lst)) == s.ascii_lowercase
