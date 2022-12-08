import numpy as np

with open('input.txt') as input_text:
    tree_matrix = np.array([np.array(list(x)) for x in input_text.read().splitlines()])


# Part 1
visible_trees = 2 * tree_matrix.shape[0] + 2 * (tree_matrix.shape[1] - 2)

for row in range(1, len(tree_matrix) - 1):
    for column in range(1, len(tree_matrix) - 1):
        a = all(tree_matrix[row][column] > trees_left for trees_left in tree_matrix[row][:column]) or all(
            tree_matrix[row][column] > trees_right for trees_right in tree_matrix[row][column + 1:])
        b = all(
            tree_matrix[row][column] > tree for tree in [tree_matrix[i][column] for i in range(row)]) or all(
            tree_matrix[row][column] > trees for trees in
            [tree_matrix[trees][column] for trees in range(row + 1, len(tree_matrix))])
        visible_trees += a or b
print(visible_trees)

# Part 2
max_score = 0
for row in range(1, len(tree_matrix) - 1):
    for column in range(1, len(tree_matrix) - 1):
        tree_score = 1
        for hor_direction, vert_direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            curr = 0
            n_row, n_col = row + hor_direction, column + vert_direction

            while 0 <= n_row < len(tree_matrix) and 0 <= n_col < len(tree_matrix[0]):
                curr += 1
                if tree_matrix[n_row][n_col] >= tree_matrix[row][column]:
                    break

                n_row += hor_direction
                n_col += vert_direction

            tree_score *= curr

        max_score = max(max_score, tree_score)
print(max_score)
