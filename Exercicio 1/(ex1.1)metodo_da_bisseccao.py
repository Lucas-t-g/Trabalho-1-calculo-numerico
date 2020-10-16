import math as mt

def func(x):
  return mt.cosh(x) - 2*mt.e**(-0.3*x)

a = 2
b = 0
i = 0
precisao = 1e-3
while(abs(a-b) > precisao):
  xzero = (a+b)/2
  if(func(a)* func(xzero) > 0 ):
    a = xzero
  else:
    b = xzero
  i += 1

print("precisão: ", precisao)
print("número de iterações: ", i)
xzero = (a+b)/2
print("f(",xzero,") = ", func(xzero))

