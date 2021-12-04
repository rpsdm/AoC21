with open("4.txt", "r") as f:
    i = [x.strip() for x in f.readlines() if x not in {"\n"}]

chosen = i[0].split(",")


class Board:
    def __init__(self, ntp: dict):
        self.ntp = ntp
        self.ptd = [False] * 25
        self.won = False

    def check_bingo(self) -> bool:
        for n in range(5):
            if all(self.ptd[5*n: 5*(n+1)]) or all([self.ptd[x+n] for x in range(0, 21, 5)]):
                return True
        return False

    def mark_number(self, number: str) -> int:
        if self.won or number not in self.ntp:
            return 0
        self.ptd[self.ntp[number]] = True
        return self.get_score(number) if self.check_bingo() else 0

    def get_score(self, called: str) -> int:
        self.won = True
        return sum(int(n) for n in self.ntp if not self.ptd[self.ntp[n]]) * int(called)


def get_boards() -> list[Board]:
    boards = []
    for n in range((len(i) - 1) // 5):
        nums = {}
        for k in range(5):
            line = [x for x in i[5*n+1+k].split(" ") if x not in {""}]
            for m in range(5):
                nums[line[m]] = k * 5 + m
        boards.append(Board(nums))
    return boards


def main():
    boards = get_boards()
    first_score = last_score = 0
    for num in chosen:
        for board in boards:
            score = board.mark_number(num)
            if score:
                last_score = score
            if not first_score:
                first_score = score
    print(first_score, last_score)


if __name__ == "__main__":
    main()
