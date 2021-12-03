setwd("/home/dominik/Coding/AoC21/Day 1")
i <- scan("1.txt")
sum(i[-length(i)] < i[-1])
sum(head(i, -3) < i[-(1:3)])
