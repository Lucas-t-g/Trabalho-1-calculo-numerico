import math as mt
from time import sleep
from numpy import arange

c = 0.3
w = 3
d = 0.6
k = 6

def funcx(x):
    return (mt.e**(-c*x)) * (mt.sin(w*x) - d*x**2) + k

def func(x):
    return ( mt.e**(-c*x) )*( w*mt.cos(w*x) - c*mt.sin(w*x) - 2*d*x + c*d*x**2 )

def funcl(x):
    return -( mt.e**(-c*x) ) * ( ((w**2)-(c**2))*mt.sin(w*x) + 2*w*c*mt.cos(w*c) - 4*c*d*x + (c**2)*d*(x**2) + 2*d )



# for j in arange(0, 2.1, 0.1):
#     print("x = {:<10.5f}) : f(x)= {:<10.5f} :: fl(x) = {:<10.5f} :: fll(x) = {:<10.5f}".format(j, funcx(j), func(j), funcl(j)))

def bisseccao(a, b):
    i = 0
    precisao = 1e-5
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
    print("raiz aproximada: fl({:^10.5f}) = {:>10.5f}".format(xzero, func(xzero)))
    print("ponto na função: f({:^10.5f}) = {:>10.5f}".format(xzero, funcx(xzero)))
    if( funcl(xzero) < 0 ):
        print("é ponto de máximo\n")
    else:
        print("é ponto de minimo\n")
    return xzero

bisseccao(0, 1)
bisseccao(1, 2)