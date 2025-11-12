def reader(filepath):
	with open(filepath) as f:
		return f.read()

from stats import counter

from stats import character_count

characters = {character_count}

def frankenstein_fetch():
	text = reader("books/frankenstein.txt")
	print(f"Found {counter(text)} total words")
	print(characters)

frankenstein_fetch()
