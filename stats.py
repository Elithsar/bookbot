def count_words(text):                                          return len(text.split())

def count_chars(text):
    char_list = {}
    text = text.lower()
    for c in text:
        if c in char_list:
            char_list[c] += 1
        else:
            char_list[c] = 1
    return char_list
