def word_count(words):
        list_of_words = words.split()
        number_of_words = len(list_of_words)
        return number_of_words

def char_count(text: str) -> dict[str, int]:
	text = text.lower()
	counts: dict[str, int] = {}
	for ch in text:
		if ch in counts:
			counts[ch] += 1
		else:
			counts[ch] = 1
	return counts

def sort_on(item):
	return item["num"]	

def to_sorted_char_list(counts: dict[str, int]) -> list[dict]:
	items = []
	for ch, count in counts.items():
		items.append({"char": ch, "num": count})
	items.sort(reverse=True, key=sort_on)
	return items