from stats import counter, character_count, report

def reader(filepath):
	with open(filepath) as f:
		return f.read()

def frankenstein_fetch():
    text = reader("books/frankenstein.txt")
    counts = character_count(text)
    sorted_chars = report(counts)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstine.txt...
----------- Word Count ----------
Found {counter(text)} total words
--------- Character Count -------
    """)
    for char_dict in sorted_chars:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

frankenstein_fetch()
