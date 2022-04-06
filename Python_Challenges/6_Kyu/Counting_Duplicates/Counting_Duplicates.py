def duplicate_count(text):
    
    from collections import Counter
    dup_count = 0
    
    for letter,occurance in Counter(text.lower()).items():
        if occurance > 1:
            dup_count += 1
    
    return dup_count
