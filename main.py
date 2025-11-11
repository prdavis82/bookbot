def reader(filepath):
	with open(filepath) as f:
		return f.read()

def frankenstein_fetch():
	filepath = "books/frankenstein.txt"
	text = reader(filepath)
	print(text)

frankenstein_fetch()
