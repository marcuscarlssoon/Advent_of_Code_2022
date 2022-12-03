import string

ALPHABET = list(" " + string.ascii_lowercase + string.ascii_uppercase)

with open('input.txt') as input_text:
    compartments = [[x[:len(x) // 2], x[len(x) // 2:]] for x in input_text.read().splitlines()]

similarities = []
for content in compartments:
    same_content = set(content[0]).intersection(set(content[1]))
    similarities.append(ALPHABET.index(same_content.pop()))

print(sum(similarities))
