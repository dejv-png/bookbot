import sys

def get_books_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

from stats import word_count

from stats import char_count

from stats import sort_on

from stats import to_sorted_char_list

def main():
	len(sys.argv) == 2
	if len(sys.argv) !=2 :
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		filepath = sys.argv[1]
		book_contents = get_books_text(filepath)
		num_words = word_count(book_contents)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {filepath}...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")

		chars = char_count(book_contents)
		items = to_sorted_char_list(chars)

		for item in items:
			ch = item["char"]
			if ch.isalpha():
				print(f"{ch}: {item['num']}")

		print("============= END ===============")

main()



