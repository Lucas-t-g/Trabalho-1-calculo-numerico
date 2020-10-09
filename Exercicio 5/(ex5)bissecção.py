import math as mt
from numpy import arange

def funcx(x):
  return ( 1-mt.e**(-0.5*x) )*( mt.sin(0.75*x) )

def func(x):
    return 0.75*mt.cos(0.75*x) - ( mt.e**(-0.5*x) )*( -0.5*mt.sin(0.75*x) + 0.75*mt.cos(0.75*x) )

def funcl(x):
    a = 0.75
    b = 0.3125
    c = 0.5625
    sin_ax = mt.sin(a*x)
    cos_ax = mt.cos(a*x)
    exp = mt.e**(-0.5*x)
    return -c*sin_ax + a*cos_ax*exp + b*sin_ax*exp

# for j in arange(2*mt.pi, 2*mt.pi+0.3, (1/50)):
#     print("x = {:<17f}) : f(x)= {:<17f} : f(x)= {:<17f} : f(x)= {:<17f}".format(j, funcx(j), func(j), funcl(j)) )

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

bisseccao(0, 2*mt.pi)
bisseccao(2*mt.pi, 0)
bisseccao((3/2)*mt.pi, mt.pi*(5/2))