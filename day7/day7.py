import os

with open('input.txt') as input_text:
    lines = input_text.read().splitlines()

base = '/'
directories = {}
sub_directories = {}

# Assume only 1 ls per directory
for line in lines:
    first, command, *args = line.split()  # first can be either '$', 'dir' or the size of a file
    if first != '$':
        if first == 'dir':
            sub_directories[base].append(os.path.normpath(os.path.join(base, command)))
        else:
            directories[base] += int(first)
        continue

    if command == 'cd':
        path, = args
        base = os.path.normpath(os.path.join(base, path))
        continue

    directories[base] = 0
    sub_directories[base] = []


def directory_size(name):
    size = directories[name]
    for sub in sub_directories[name]:
        size += directory_size(sub)
    return size


# Part 1
total_sizes = [directory_size(directory) for directory in directories if directory_size(directory) <= 100000]
print(sum(total_sizes))

# Part 2
sum_total_size = directory_size('/')
unused = 70000000 - sum_total_size
min_size = None
for directory in directories:
    size = directory_size(directory)
    if unused + size >= 30000000 and (min_size is None or min_size > size):
        min_size = size
print(min_size)
