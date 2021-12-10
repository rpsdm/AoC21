with open("8.txt", "r") as f:
    i = f.read().splitlines()

# Part 1
counter = 0
for line in i:
    for word in line.split(" | ")[1].split():
        if len(word) in {2, 3, 4, 7}:
            counter += 1
print(counter)

acc = 0
# Part 2
for line in i:
    puzzle, output = line.split(" | ")
    puzzle = puzzle.split(" ")
    output = output.split(" ")
    numbers = [""] * 10
    # 1 4 7 8
    for num in puzzle:
        match len(num):
            case 2:
                numbers[1] = num
            case 4:
                numbers[4] = num
            case 3:
                numbers[7] = num
            case 7:
                numbers[8] = num
            case _:
                pass
    for i in {1, 4, 7, 8}:
        puzzle.remove(numbers[i])

    # 6
    E = [x for x in numbers[8] if x not in numbers[1]]
    for num in puzzle:
        if all([x in num for x in E]):
            numbers[6] = num
    puzzle.remove(numbers[6])

    # 5 9
    for num in puzzle:
        if len(num) in {5} and all([x in numbers[6] for x in num]):
            numbers[5] = num
        if len(num) in {6}:
            if all([x in num for x in numbers[7]]) and all([x in num for x in numbers[4]]):
                numbers[9] = num
    for i in {5, 9}:
        puzzle.remove(numbers[i])

    # 0 2
    for num in puzzle:
        if len(num) in {5} and any([x not in numbers[9] for x in num]):
            numbers[2] = num
        if len(num) in {6}:
            numbers[0] = num
    for i in {2, 0}:
        puzzle.remove(numbers[i])

    # 3
    numbers[3] = puzzle[0]

    value = ""
    for num in output:
        for n in numbers:
            if len(n) in {len(num)} and all([x in n for x in num]):
                value += str(numbers.index(n))
    acc += int(value)

print(acc)
