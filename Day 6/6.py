with open("6.txt", "r") as f:
    i = f.readlines()[0].split(",")

lf = [0]*9
for x in i:
    lf[int(x)] += 1

for n in {80, 256-80}:
    for _ in range(n):
        zeros = lf[0]
        lf[0:8] = lf[1:9]
        lf[6] += zeros
        lf[8] = zeros
    print(sum(lf))