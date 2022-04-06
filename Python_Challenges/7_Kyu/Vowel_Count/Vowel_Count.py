def get_count(sentence):
    vowels = 'aeiou'
    counter = [x for x in sentence if x in vowels]
    return len(counter)
