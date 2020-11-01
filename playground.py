def build_n(n):

    grid = [[1, 2, 3], [2, 3, 6]]

    for row in grid:
        row.insert(0, 0)
        row.append(0)

    grid.insert(0, [0] * (len(grid[0]) + 1))
    grid.append([0] * (len(grid[0]) + 1))

    print(grid)

def main():
    print(build_n(11))

if __name__ == '__main__':
    main()
