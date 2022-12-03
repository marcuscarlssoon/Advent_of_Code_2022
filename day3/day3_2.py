import string

ALPHABET = list(" " + string.ascii_lowercase + string.ascii_uppercase)

with open('input.txt') as input_text:
    lines = input_text.read().splitlines()

similarities = []
for i in range(0, len(lines), 3):
    shared_letter = set(lines[i]).intersection(set(lines[i + 1]), set(lines[i + 2]))
    similarities.append(ALPHABET.index(shared_letter.pop()))

print(sum(similarities))
