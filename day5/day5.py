stacks = {
    1: list('FDBZTJRN'),
    2: list('RSNJH'),
    3: list('CRNJGZFQ'),
    4: list('FVNGRTQ'),
    5: list('LTQF'),
    6: list('QCWZBRGN'),
    7: list('FCLSNHM'),
    8: list('DNQMTJ'),
    9: list('PGS'),
}  # If it looks stupid but it works, it ain't stupid

with open('input.txt') as instruction_text:
    lines = [line.split() for line in instruction_text.read().splitlines()]

for line in lines:
    new_stack = int(line[-1])
    old_stack = int(line[3])
    amount = int(line[1])

    # For answer on part B, remove "reversed"
    stacks[new_stack] += list(reversed(stacks[old_stack][len(stacks[old_stack]) - amount:]))
    stacks[old_stack] = stacks[old_stack][:amount * -1]

last_item = ""
for stack in stacks.values():
    last_item += stack[-1]

print(last_item)
