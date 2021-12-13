with open("13.txt", "r") as f:
    i = f.read().splitlines()
dots = [tuple(map(int, line.split(","))) for line in i if "," in line]
inst = [(line[11], int(line[13:])) for line in i if "=" in line]

first = True
for i, (k, d) in enumerate(inst):
    ndots = set()
    if k in {"x"}:
        for px, py in dots:
            ndots.add((2*d-px, py)) if px > d else ndots.add((px, py))
    else:
        for px, py in dots:
            ndots.add((px, 2*d-py)) if py > d else ndots.add((px, py))

    dots = ndots
    # Part 1
    if i == 0:
        print(len(ndots))

# Part 2
dlist = [[" " for _ in range(max(x for x, _ in dots)+1)] for _ in range(max(y for _, y in dots)+1)]
for x, y in dots:
    dlist[y][x] = "@"
print("\n".join("".join(line) for line in dlist))
