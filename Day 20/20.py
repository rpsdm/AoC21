with open("20.txt", "r") as f:
    i = f.read().splitlines()
alg = i[0]
img = [[k for k in line] for line in i[2:]]


def extend(mt: list, by: int):
    for n in range(len(mt)):
        mt[n] = ["."] * by + mt[n] + ["."] * by
    for _ in range(by):
        mt = [["."] * len(mt[0])] + mt + [["."] * len(mt[0])]
    return mt


def enhance(mt: list, by: int):
    for b in range(by):
        cpy = [["."] * len(mt[0]) for _ in range(len(mt))]
        for r in range(len(mt)):
            for c in range(len(mt[0])):
                if r in {0, len(mt)-1} or c in {0, len(mt[0])-1}:
                    val = mt[0][0]*8
                else:
                    val = mt[r-1][c-1] + mt[r-1][c] + mt[r-1][c+1] \
                        + mt[r][c-1] + mt[r][c] + mt[r][c+1] \
                        + mt[r+1][c-1] + mt[r+1][c] + mt[r+1][c+1]
                val = val.replace(".", "0").replace("#", "1")
                cpy[r][c] = alg[int(val, 2)]
        mt = [line.copy() for line in cpy]
    return mt


def solve(n: int):
    res = enhance(extend(img, n+1), n)
    return sum(line.count("#") for line in res[1:-1])


if __name__ == "__main__":
    print(solve(2))
    print(solve(50))
