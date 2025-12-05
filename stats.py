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

def sort_on(item):
    return item["num"]

def report(letter_count):
    results = []
    for ch, cnt in letter_count.items():
        if ch.isalpha():
            results.append({"char": ch, "num": cnt})
    results.sort(reverse=True, key=sort_on)
    return results
