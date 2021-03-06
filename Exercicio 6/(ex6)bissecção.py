import math as mt
from numpy import arange

g = 9.8
c = 14
v = 35
t = 7


def func(m):
    return v - (g*m*(1 - mt.e**( (-c/m)*t ) ))/c

def funcv(m):
    return (g*m*(1 - mt.e**( (-c/m)*t ) ))/c

# for j in arange(0, 100, 10):
#     print("x = {:<4} : f(x)= {:<17f} : fv(x)= {:<17f}".format(j, func(j), funcv(j)) )

def bisseccao(a, b):
    i = 0
    precisao = 1e-2
    while(abs(a-b) > precisao):
        xzero = (a+b)/2
        if(func(a) * func(xzero) > 0 ):
            a = xzero
        else:
            b = xzero
        i += 1
        # print(a, b)
        # print("f({:^10.5f})= {:<10.5f} :: f({:^10.5f})= {:<10.5f}".format(a, func(a), b, func(b)))

    print("precisão: {:^10.5f}".format(precisao) ) 
    print("número de iterações: {:^10}".format( i))
    xzero = (a+b)/2
    print("raiz aproximada: f({:^10.5f}) = {:>10.5f}".format(xzero, func(xzero)))

    return xzero

bisseccao(1, 100)