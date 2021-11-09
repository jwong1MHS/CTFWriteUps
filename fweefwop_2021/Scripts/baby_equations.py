from z3 import *

x = Int('x')
y = Int('y')

solve(2*x*x+3*y==5*x*x+4*y*y)
