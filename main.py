def reader(filepath):
	with open(filepath) as f:
		return f.read()

from stats import counter

from stats import character_count

def frankenstein_fetch():
	text = reader("books/frankenstein.txt")
	char_dict = character_count(text)
	print(f"Found {counter(text)} total words")
	print(char_dict)

frankenstein_fetch()
