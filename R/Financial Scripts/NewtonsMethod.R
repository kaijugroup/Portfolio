# Program to calculate the root of a function using Newton's Method.  Currently requires the function and
# and its derivative to be entered in functions f1 and df1.  

newtons <- function(n, a, b) {
  i <- 0
  g = (a+b)/2 #starting guess for the middle of the range
  while (i<=n) {
    x <- f1(g)
    dx <- df1(g)
    ng <- g - (x/dx)
    g <- ng
    i <- i+1
  }
  g
}

f1 <- function(x) {
  y <- cos(x)-x  #input function
  return(y)
}

df1 <- function(x) {
  y <- (-sin(x))-1  #input first derivative of function
  return(y)
}

newtons(10000, 0, 2)
