with open("11.txt", "r") as f:
    i = [int(x) for x in f.read().replace("\n", "")]


def ind(r, c):
    return 10 * r + c


def valid(r, c):
    return 0 <= r < 10 and 0 <= c < 10


def adj(r, c):
    return [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r,     c - 1),             (r,     c + 1),
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]


def safeadj(r, c):
    return [(ar, ac) for ar, ac in adj(r, c) if valid(ar, ac)]


flashes = 0
first_all = 0
step = 0
while any(k != 0 for k in i):
    i = [x + 1 for x in i]
    while any(n > 9 for n in i):
        for x in range(10):
            for y in range(10):
                if i[ind(x, y)] > 9:
                    for ax, ay in safeadj(x, y):
                        i[ind(ax, ay)] += 1
                    i[ind(x, y)] = -99
    i = [0 if n < 0 else n for n in i]
    flashes += i.count(0)
    step += 1

    if step == 100:
        print(flashes)   # Part 1

print(step)  # Part 2
