def count_words(text):                                          return len(text.split())

def sort_on(d):
    return d["count"]

def count_chars(text):
    char_list = {}
    text = text.lower()
    for c in text:
        if c in char_list:
            char_list[c] += 1
        else:
            char_list[c] = 1
    return char_list

def count_chars_sorted(text):
    char_list = count_chars(text)
    sorted_list = []
    for char in char_list:
        sorted_list.append({
            "char": char,
            "count": char_list[char]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

