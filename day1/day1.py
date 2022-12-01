test = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

with open('input.txt') as input_text:
    lines = [x for x in list(input_text.read().splitlines())]

    calories_per_elve = []
    sum_individual = 0

    for line in lines:
        if line != '':
            sum_individual += int(line)
        else:
            calories_per_elve.append(sum_individual)
            sum_individual = 0

    print(f"Answer part 1: {max(calories_per_elve)}")

    # Part 2
    sorted_acc = sorted(calories_per_elve, reverse=True)
    print(f"Answer part 2: {sum(sorted_acc[:3])}")
