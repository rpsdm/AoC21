with open("7.txt", "r") as f:
    i = list(map(int, f.readlines()[0].split(",")))

# Part 1
i = sorted(i)
m = (i[len(i)//2-1] + i[len(i)//2])//2
n = list(map(lambda x: abs(x-m), i))
print(sum(n))

# Part 2
m = sum(i)//len(i)
n = list(map(lambda x: abs(x-m), i))
n = list(map(lambda x: x*(x+1)//2, n))
print(sum(n))