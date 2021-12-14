with open("14.txt", "r") as f:
    i = f.read().splitlines()
poly = list(i[0])
rules = {n.split(" -> ")[0]: n.split(" -> ")[1] for n in i[2:]}

polyd = {}
for k in range(1, len(poly)):
    part = "".join(poly[k-1:k+1])
    polyd[part] = 1 if part not in polyd else polyd[part] + 1

for n in range(1, 41):
    polydn = {}
    for k, v in polyd.items():
        if k in rules:
            polydn[k[0] + rules[k]] = v if k[0] + rules[k] not in polydn else polydn[k[0] + rules[k]] + v
            polydn[rules[k] + k[1]] = v if rules[k] + k[1] not in polydn else polydn[rules[k] + k[1]] + v
        else:
            polydn[k] = v
        polyd = polydn
    if n in {10, 40}:  # Part 1 2
        elem = {}
        for k, v in polyd.items():
            elem[k[0]] = v if k[0] not in elem else elem[k[0]] + v
            elem[k[1]] = v if k[1] not in elem else elem[k[1]] + v
        print((max(elem.values()) - min(elem.values())-1) // 2)
