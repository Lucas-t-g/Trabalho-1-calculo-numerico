import math as mt
from time import sleep
from numpy import arange

a = -30
b = 15
l = 120

def func(x):
    return -(1/x)*(mt.sinh(a*x) - mt.sinh(b*x)) - l

def funcl(x):
    return -(a/x)*mt.cosh(a*x) + (x**-2)*mt.sinh(a*x) +(b/x)*mt.cosh(b*x) - (x**-2)*mt.sinh(b*x)

# possivel intervalo
inicio = 0.08
fim = 0.12

x1 = inicio
precisao = 1e-5
i = 1
x2 = x1-func(x1)/funcl(x1)
# print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))
# print("k{} : fl({:<10.5f}) = {:<10.5f} : f({:<10.5f}) = {:<10.5f}".format(i, x1, funcl(x1), x1, func(x1)))
# print("k{} : x1 = {:<10.5f} : x2 = {:<10.5f}  :: f({:^10.5f}) = {:<10.5f}".format(i, x1, x2, x2, func(x2)) )
while( abs(x2-x1) > precisao):
    i += 1
    x1 = x2
    x2 = x1-func(x1)/funcl(x1)
    # print("k{} : fite(x1) = {:<10.5f} : {:<10.5f} - {:<10.5f} = {:<10.5f}".format(i, x1, x2, x1, x2-x1 ))
    # print("k{} : fl({:<10.5f}) = {:<10.5f} : f({:<10.5f}) = {:<10.5f}".format(i, x1, funcl(x1), x1, func(x1)))
    # print("k{} : x1 = {:<10.5f} : x2 = {:<10.5f}  :: f({:^10.5f}) = {:<10.5f}".format(i, x1, x2, x2, func(x2)) )
    # sleep(1)

print("precisão: ", precisao)
print("número de iterações: ", i)
print("raiz aproximada: f({:<10}) = {:<10}".format(x2, func(x2)))