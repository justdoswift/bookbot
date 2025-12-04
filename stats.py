def get_book_text(path):
    text = ""
    with open(path) as f:
        text = f.read()

    return text

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_counting_characters(text):
    dict = {}

    text = text.lower()

    for t in text:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1

    return dict

def sort_count(dict):
    list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        list.append(new_dict)
    return list
