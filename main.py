def reader(filepath):
	with open(filepath) as f:
		return f.read()


def frankenstein_fetch():
	text = reader("books/frankenstein.txt")
	print(f"Found {counter(text)} total words")

def counter(text):
	return len(text.split())

frankenstein_fetch()
