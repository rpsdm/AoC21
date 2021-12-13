with open("12.txt", "r") as f:
    i = [line.split("-") for line in f.read().splitlines()]

graph = {"end": []}
for x, y in i:
    x, y = (y, x) if y in {"start"} or x in {"end"} else (x, y)
    graph[x] = [y] if x not in graph else graph[x] + [y]
    if x in {"start"} or y in {"end"}:
        continue
    graph[y] = [x] if y not in graph else graph[y] + [x]


def traverse1(current: str, path=None):
    np = set(k for k in path) if path else set()
    np.add(current)
    whereto = {k for k in graph[current] if k.isupper() or k not in np}
    return (1 if current == "end" else 0) if not whereto else sum(traverse1(n, np) for n in whereto)


def traverse2(current: str, path=None):
    np = {k: v for k, v in path.items()} if path else {}
    np[current] = 1 if current not in np else np[current] + 1
    twice = any(np[k] > 1 for k in np if k.islower())
    whereto = graph[current] if not twice else {k for k in graph[current] if k.isupper() or k not in np}
    return (1 if current == "end" else 0) if not whereto else sum(traverse2(n, np) for n in whereto)


# Part 1
print(traverse1("start"))
# Part 2
print(traverse2("start"))
