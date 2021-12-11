with open("10.txt", "r") as f:
    i = f.read().splitlines()

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores2 = {"(": 1, "[": 2, "{": 3, "<": 4}

score = 0
points = []

for line in i:
    parser = []
    for char in line:
        if char in pairs.keys():
            parser.append(char)
        else:
            if pairs[parser[-1]] == char:
                parser.pop(-1)
            else:
                score += scores1[char]
                break
    else:  # Part 2
        pts = 0
        for x in reversed(parser):
            pts *= 5
            pts += scores2[x]
        points.append(pts)
print(score)
print(sorted(points)[len(points)//2])
