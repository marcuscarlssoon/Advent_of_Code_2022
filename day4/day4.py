with open('input.txt') as input_text:
    pairs = [x.split(',') for x in input_text.read().splitlines()]

counter_a = 0
counter_b = 0
for pair in pairs:

    a = range(int(pair[0].split('-')[0]), (int(pair[0].split('-')[1]) + 1))
    b = range(int(pair[1].split('-')[0]), (int(pair[1].split('-')[1]) + 1))

    if all(x in b for x in a) or all(x in a for x in b):
        counter_a += 1

    if any(x in b for x in a) or any(x in a for x in b):
        counter_b += 1

print(counter_a)
print(counter_b)
