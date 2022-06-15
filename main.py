def is_new_submarine(mat, row, col, visited):
    if 0 <= row < len(mat) and 0 <= col < len(mat[row]) and mat[row][col] == 'X' and not visited[row][col]:
        visited[row][col] = True

        is_new_submarine(mat, row, col + 1, visited)
        is_new_submarine(mat, row, col - 1, visited)
        is_new_submarine(mat, row + 1, col, visited)

        return True
    else:
        return False


def count_submarines(mat):
    count = 0
    visited = [[False] * len(row) for row in mat]

    for row in range(len(mat)):
        for col in range(len(mat[row])):

            if is_new_submarine(mat, row, col, visited):
                count += 1

    # for r in visited:
    #     print(r)

    return count


mat = [
        ['X', 'X', 'X', ' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ', 'X', ' ', ' '],
        ['X', 'X', 'X', ' ', 'X', ' ', 'X'],
        ['X', 'X', 'X', ' ', 'X', ' ', ' '],
        ['X', 'X', 'X', ' ', ' ', ' ', ' '],
        ]

print(count_submarines(mat))


