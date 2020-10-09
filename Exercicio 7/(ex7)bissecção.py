import math as mt
from numpy import arange

a = -0.001
b = 1.6
w = 0.01*mt.pi

def funcr(x):
    numerador = b*mt.sin(w*x)
    denominador = 2 - (mt.e**(a*x)) 
    return 20 + ( numerador / denominador )


for j in arange(0, 50, 5):
    print("x = {:<17f}) : f(x)= {:<17f} : f(x)= {:<17f} : f(x)= {:<17f}".format(j, funcr(j), 1, 1) )

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
