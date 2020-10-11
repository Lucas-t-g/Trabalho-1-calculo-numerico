import math as mt

def func(x):
   return mt.cosh(x) - 2*mt.e**(-0.3*x)

def funcl(x):
    return mt.sinh(x) + 0.6*mt.e**(-0.3*x)

a = 2
b = 0
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