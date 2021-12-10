with open("9.txt", "r") as f:
    i = [int(x) for x in f.read().replace("\n", "")]


def is_valid(row: int, col: int):
    return not (row < 0 or row > 99 or col < 0 or col > 99)


def p(row: int, col: int):
    return i[100 * row + col]


# Part 1
count = 0
lows = []  # for Part 2
for x in range(100):
    for y in range(100):
        lowest = True
        for ax, ay in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if is_valid(ax, ay) and p(x, y) >= p(ax, ay):
                lowest = False
        if lowest:
            count += p(x, y) + 1
            lows.append((x, y))  # for Part 2
print(count)


# Part 2
def basin(x0: int, y0: int):
    visited = []
    to_visit = [(x0, y0)]
    acc = 0
    while to_visit:
        nx, ny = to_visit[-1]
        visited.append((nx, ny))
        to_visit.pop(-1)
        if not is_valid(nx, ny) or p(nx, ny) in {9}:
            continue
        acc += 1
        for xy in [(nx - 1, ny), (nx + 1, ny), (nx, ny - 1), (nx, ny + 1)]:
            if xy not in visited and xy not in to_visit:
                to_visit.append(xy)
    return acc


basins = sorted([basin(x, y) for x, y in lows], reverse=True)
print(basins[0]*basins[1]*basins[2])
