def alphabet_position(text):
    
    import string
    
    alpha_lst = list(string.ascii_lowercase)
    
    numbered_lst = [str(alpha_lst.index(letter) + 1) for letter in text.lower() if letter.isalpha()]  
    
    return " ".join(numbered_lst)
