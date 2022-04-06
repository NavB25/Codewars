def order(sentence):
    lst = []
    for x in range(1,10):
        for word in sentence.split():
            if str(x) in word:
                lst.append(word)
            else:
                continue
    return " ".join(lst)
