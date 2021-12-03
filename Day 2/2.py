with open("2.txt", "r") as f:
    i = f.read().splitlines()
# Part 1
horizontal = depth = 0
for x in i:
    n = int(x.split()[1])
    if x.startswith("f"):
        horizontal += n
    elif x.startswith("u"):
        depth -= n
    elif x.startswith("d"):
        depth += n
print(horizontal*depth)

# Part 2
horizontal = depth = aim = 0
for x in i:
    n = int(x.split()[1])
    if x.startswith("f"):
        horizontal += n
        depth += aim*n
    elif x.startswith("u"):
        aim -= n
    elif x.startswith("d"):
        aim += n
print(horizontal*depth)
