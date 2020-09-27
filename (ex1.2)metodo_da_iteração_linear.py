import math as mt

def func(x):
  return -2 + 7*x - 5*x**2 + 6*x**3

def funcIte(x):
  return (2 + 5*x**2 - 6*x**3)/7

a = -1
b = 1
x1 = b
precisao = 1e-3
i = 1
# x1 = 0.5
x2 = funcIte(x1)
# print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))

while( abs(x2-x1) > precisao):
  i += 1
  x1 = x2
  x2 = funcIte(x1)
  # print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))

print("precisão: ", precisao)
print("[b, a] = [", b, ",", a, "]")
print("número de iterações: ", i)
print("raiz aproximada: f({:<10}) = {:<10}".format(x2, func(x2)))