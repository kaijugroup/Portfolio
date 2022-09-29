# Program to calculate the root of a function using Newton's Method.  Currently requires the function and
# and its derivative to be entered in functions f1 and df1.  

newtons <- function(n, a, b) {
  i <- 0
  g = (a+b)/2
  while (i<=n) {
    g+1
  }
  return(g)
}

f1 <- function(x) {
  y <- x+1
  return(y)
}

df1 <- function(x) {
  y <- 1
  return(y)
}