import sys

def make_2d_grid() -> list[list[int]]:
    grid: list[list[int]] = []
    square_size: int = 8
    single_row = [0] * square_size
    for i in range(square_size):
        grid.append(single_row.copy())

    return grid


if __name__ == '__main__':
    list2d = make_2d_grid()
    print(f'{list2d=}')

    for i in range(len(list2d)):
        for j in range(len(list2d[i])):
            if i < 3 or i > 4:
                list2d[i][j] = 1

    print(f'{list2d=}')
