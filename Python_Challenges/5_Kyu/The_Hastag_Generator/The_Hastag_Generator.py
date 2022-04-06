def generate_hashtag(s):
    hashtag = '#' + ''.join([word.capitalize() for word in s.split()])
    return hashtag if len(hashtag) in range(1,141) and s != '' else False
