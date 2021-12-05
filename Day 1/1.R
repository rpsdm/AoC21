setwd("~/Coding/AoC21/Day 1")
i <- scan("1.txt")
# Part 1
sum(i[-length(i)] < i[-1])
# Part 2
sum(head(i, -3) < i[-(1:3)])
