with open('input.txt') as input_text:
    input_data = [*input_text.read()]


def n_unique_characters(n):
    data = input_data.copy()
    for i in range(n, len(data)):
        if len(set(data[:n])) == n:
            print(i)
            break
        data.pop(0)


n_unique_characters(4)
n_unique_characters(14)
