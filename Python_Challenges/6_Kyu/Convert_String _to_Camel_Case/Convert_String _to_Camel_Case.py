def to_camel_case(text):
    
    lst = ''
    position = 0 #index position of underscore/dash 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(text)):
            
            #if statement will add letters from the inputted text into the lst variable before coming across a dash/underscore in text
            if position == 0:
                if text[i].lower() in alphabet:
                    lst += text[i]
                else:
                    position = i
            
            #once a dash/underscore has been encountered, position variable was updated to mark index position.    
            else:
                #if the next iteration in the for loop is the letter that comes after dash/underscore, capitalize.
                if i == position + 1:
                    lst += text[i].upper()
                elif text[i].lower() in alphabet:
                    lst += text[i]
                else:
                    position = i        
    return lst
