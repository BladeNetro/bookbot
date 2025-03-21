import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_words_count
from stats import get_character_count
from stats import get_character_dict_list
from stats import get_sorted


def main():
	for book_path in sys.argv:
		text = get_book_text(book_path)
		num_words = get_words_count(text)
		num_characters_dict = get_character_count(text)
		chars_dict_list = get_character_dict_list(num_characters_dict)
		sorted_chars = get_sorted(chars_dict_list)


		print("=========== BOOKBOT ===========")
		print(f"Analyzing book found at {book_path}...")
		print("---------- Word Count ---------")
		print(f"Found {num_words} total words")
		for item in sorted_chars:
			if not item["char"].isalpha():
				continue
		print(f"{item["char"]}: {item["count"]}")
		print("============= END =============")


def get_book_text(path):
	with open(path) as file:
		return file.read()


main()