def get_num_words(text):
    return len(text.split())
def count_characters(text):
    char_count = {}
    
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    
    return char_count


def list_of_dictionaries(dic_char):
    new_list = []


    for key in dic_char:
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = dic_char[key]
        new_list.append(new_dic)
    new_list.sort(reverse=True,key=sort_on)

    for ay_7aga in new_list:
        if ay_7aga["char"].isalpha():
            print(f"{ay_7aga['char']}: {ay_7aga['num']}")

    print("============= END ===============")
    
def sort_on(fuse):
    return fuse["num"]
