def get_words_count(text):
	num_words = text.split()
	return len(num_words)


def get_character_count(text):
	character_dict = {}
	text = text.lower()
	for character in text:
		if character in character_dict:
			character_dict[character] += 1
		else:
			character_dict[character] = 1
	return character_dict


def get_character_dict_list(num_characters_dict):
	keys_list = list(num_characters_dict.keys())
	values_list = list(num_characters_dict.values())
	chars_dict_list = []
	for x in range(0, len(keys_list)):
		characters_dict = {}
		characters_dict["char"] = keys_list[x]
		characters_dict["count"] = values_list[x]
		chars_dict_list.append(characters_dict)
	return chars_dict_list


def get_sorted(chars_dict_list):
	chars_dict_list.sort(key=lambda e: e["count"], reverse=True)
	return chars_dict_list
