def get_num_words(file_string):
    return len(file_string.split())


def count_character(file_string):
    character_dict = {}

    for character in file_string:
        count = 1
        if character.lower() in character_dict:
            character_dict[character.lower()] += count
        else:
            character_dict[character.lower()] = count

    return character_dict


def sorted_list(char_dict):
    new_list = []
    for k in char_dict:
        if k.isalpha():
            new_dict = {"char": k, "num": char_dict[k]}
            new_list.append(new_dict)

    new_list.sort(reverse=True, key=lambda dict: dict["num"])

    return new_list
