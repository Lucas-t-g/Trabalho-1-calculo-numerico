import math as mt

def func(x):
   return -2 + 7*x - 5*x**2 + 6*x**3

def funcl(x):
    return 7 - 10*x + 18*x**2

a = 1
b = -1
x1 = b
precisao = 1e-3
i = 1
x2 = x1-(func(x1)/funcl(x1))
# print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))
while( abs(x2-x1) > precisao):
    i += 1
    x1 = x2
    x2 = x1-(func(x1)/funcl(x1))
    # print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))

print("precisão: ", precisao)
print("[b, a] = [", b, ",", a, "]")
print("número de iterações: ", i)
print("raiz aproximada: f({:<10}) = {:<10}".format(x2, func(x2)))