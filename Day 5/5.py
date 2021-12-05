with open("5.txt", "r") as f:
    i = [list(map(int, line.split(","))) for line in f.read().replace(" -> ", ",").splitlines()]

# Part 1
points = {}
for (x1, y1, x2, y2) in i:
    if x1 != x2 and y1 != y2:
        continue
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1
    for x in range(x1, x2+dx, dx):
        for y in range(y1, y2+dy, dy):
            points[(x, y)] = 1 if (x, y) not in points else points[(x, y)] + 1
print(sum(1 for p in points if points[p] not in {1}))

# Part 2
for (x1, y1, x2, y2) in i:
    if x1 == x2 or y1 == y2:
        continue
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1
    while x1 != x2+dx:
        points[(x1, y1)] = 1 if (x1, y1) not in points else points[(x1, y1)] + 1
        x1 += dx
        y1 += dy
print(sum(1 for p in points if points[p] not in {1}))
