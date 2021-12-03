with open("1.txt", "r") as f:
    i = [int(x) for x in f.read().splitlines()]
# Part 1
print(sum([x < y for (x, y) in zip(i[:-1], i[1:])]))
# Part 1
print(sum(([x < y for (x, y) in zip(i[:-3], i[3:])])))

# Part 2 alt
n = [x + y + z for (x, y, z) in zip(i, i[1:], i[2:])]
print(sum([x < y for (x, y) in zip(n[:-1], n[1:])]))
