from stats import counter, character_count, report

def reader(filepath):
	with open(filepath) as f:
		return f.read()

def frankenstein_fetch():
    text = reader("books/frankenstein.txt")
    counts = character_count(text)
    sorted_chars = report(counts)
    print(f"Found {counter(text)} total words")
    print(sorted_chars)

frankenstein_fetch()
