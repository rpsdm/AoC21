setwd("/home/dominik/Coding/AoC21/Day 3")
i <- scan("3.txt", what="")

# Part 1
gamma <- ""
for (x in 1:nchar(i[1])) {
  n <- table(substr(i, x, x))
  gamma <- paste0(gamma, names(n[n == max(n)]))
}
gamma <- strtoi(gamma, base=2)
epsilon <- strtoi(strrep("1", nchar(i[1])), base=2) - gamma
gamma*epsilon

# Part 2
oxigen <- i
n <- 1
while (length(oxigen) > 1) {
  s <- table(substr(oxigen, n, n))
  oxigen <- oxigen[substr(oxigen, n, n) == max(names(s[s == max(s)]))]
  n <- n+1
}
co2 <- i
n <- 1
while (length(co2) > 1) {
  s <- table(substr(co2, n, n))
  co2 <- co2[substr(co2, n, n) == min(names(s[s == min(s)]))]
  n <- n+1
}
strtoi(oxigen, base=2)*strtoi(co2, base=2)
