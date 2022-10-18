n <- 120
payment <- 132.16
int <- 0.10
startprin <- 10000.00

fnum <- function(n) {
  return(round(n, digits=2))
}

amort <- data.frame(matrix(ncol=5, nrow=n))
colnames(amort) <- c('Time','Payment','Int Paid','Prin Padi','Out Prin')

i <- 1
outprin <- startprin
while (i < (n+1)) {
  intpaid <- (int/12)*outprin
  prinpaid <- payment-intpaid
  newprin <- outprin-prinpaid
  amort[i,] = c(fnum(i), fnum(payment), fnum(intpaid), fnum(prinpaid), fnum(newprin))
  outprin <- newprin
  i <- i+1
}

amort