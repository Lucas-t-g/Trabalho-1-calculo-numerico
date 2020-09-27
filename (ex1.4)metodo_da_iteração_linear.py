import math as mt

def func(x):
  return (0.9 - 0.4*x)/x

def funcIte(x):
  return 0.9/0.4

a = 3
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