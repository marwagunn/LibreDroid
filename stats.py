def get_words(filepath):
    with open(filepath) as f:
     return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)


def get_chars(text):
    chars={}

    for c in text:
        lowerC = c.lower()
        if lowerC in chars:
            chars[lowerC]+=1
        else:
            chars[lowerC]=1

    return chars

def sort_on(c):
    return c["num"]


def sort_chars_dict(chars):
    chars_list= []
    for c in chars :
        chars_list.append({"char":c,"num":chars[c]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list