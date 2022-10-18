#Program for printing binomial and multinomial expansions

binom <- function(a,b,n) {
  k <- 0
  while (k<(n+1)) {
    coeff <- factorial(n)/((factorial(k))*(factorial(n-k)))
    bpower <- n-k
    print(paste(coeff, a,'^',k,"*",b,"^",bpower))
    k <- k+1
  }
}

binom('a','b',3)