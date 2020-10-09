import math as mt
from numpy import arange

def func(x):
  return ( 1-mt.e**(-0.5*x) )*( mt.sin(0.75*x) )

# for j in arange(-1, 2*mt.pi, 0.5):
#     print("x = {:<10.5f}) : f(x)= {:<10.5f}".format(j, func(j)))

def bisseccao(a, b):
    i = 0
    precisao = 1e-2
    while(abs(a-b) > precisao):
        xzero = (a+b)/2
        if(func(a)* func(xzero) > 0 ):
            a = xzero
        else:
            b = xzero
        i += 1
        # print("f({:^10.5f})= {:<10.5f} :: f({:^10.5f})= {:<10.5f}".format(a, func(a), b, func(b)))

    print("precisão: {:^10}".format(precisao) )
    print("número de iterações: {:^10}".format( i))
    xzero = (a+b)/2
    print("f({:^10f}) = {:>10f}\n".format(xzero, func(xzero)))

bisseccao(0, 2*mt.pi)
bisseccao(2*mt.pi, 0)
