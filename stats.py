def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    # empty dict
    char_count = {}

    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # return dict
    return char_count

def sort_dict(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)
