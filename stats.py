def counter(text):
        return len(text.split())

def character_count(text):
	lower_case = str.lower(text)
	letter_count = {}
	for letter in lower_case:
		if letter in letter_count:
			letter_count[letter] += 1
		else:
			letter_count[letter] = 1
	return letter_count
