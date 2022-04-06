def pig_it(text):
    import re
    lst = []

    for word in text.split():
        if word[0].isalpha() and word[-1].isalpha():
            new_word = re.sub('^.','',word) + word[0] + 'ay'
            lst.append(new_word)
        elif word[0].isalpha() and word[-1].isalpha() == False:
            new_word = re.sub('^.|.$','',word)+ word[0] +'ay' + word[-1]
            lst.append(new_word)
        else:
            lst.append(word)
        
    return' '.join(lst)
