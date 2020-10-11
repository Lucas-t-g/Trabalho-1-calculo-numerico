import math as mt

def func(x):
  return -0.4*x**2 + 2.2*x + 4.7

def funcIte(x):
  return (0.4*x**2 - 4.7)/2.2

# PRIMEIRA RAIZ
a = 1
b = -5
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

print("primeira raiz")
print("precisão: ", precisao)
print("[b, a] = [", b, ",", a, "]")
print("número de iterações: ", i)
print("raiz aproximada: f({:<10}) = {:<10}".format(x2, func(x2)))

# SEGUNDA RAIZ
a = 10
b = 5
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

print("\nsegunda raiz não funciona por este método")
print("precisão: ", precisao)
print("[b, a] = [", b, ",", a, "]")
print("número de iterações: ", i)
print("raiz aproximada: f({:<10}) = {:<10}".format(x2, func(x2)))
print("não encontra a segunda raiz pois o modulo da derivada da fi no intervalo é superior a 1")