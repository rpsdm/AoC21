setwd("~/Coding/AoC21/Day 7")
i <- scan("7.txt", sep=",")
# Part 1
print(sum(abs(i-median(i))))
# Part 2
print(sum(sapply(abs(i-floor(mean(i))), function(x) x*(x+1)/2)))
