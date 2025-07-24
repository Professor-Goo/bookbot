def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict_item):
    return dict_item["num"]

def get_chars_report(chars_dict):
    chars_list = []
    for char in chars_dict:
        if char.isalpha():
            chars_list.append({"char": char, "num": chars_dict[char]})
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list