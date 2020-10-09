import math as mt

def func(x):
  return (0.9 - 0.4*x)/x

a = 3
b = 1
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
print("raiz aproximada: f(",xzero,") = ", func(xzero))

