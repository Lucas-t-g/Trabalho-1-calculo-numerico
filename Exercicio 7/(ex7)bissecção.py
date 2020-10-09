import math as mt
from numpy import arange
import matplotlib.pyplot as plt

a = -0.001
b = 1.6
w = 0.01*mt.pi

def funcr(x):
    exp = mt.e**(a*x)
    numerador = b*mt.sin(w*x)
    denominador = 2 - (exp)
    return 20 + ( numerador / denominador )

def func(x):
    cos = mt.cos(w*x)
    sen = mt.sin(w*x)
    exp = mt.e**(a*x)
    numerador = b*( ( w*cos*(2-exp) ) + ( a*sen*exp ) )
    denominador = (2 - (exp) )**2
    return numerador/denominador

def funcl(x):
    cos = mt.cos(w*x)
    sen = mt.sin(w*x)
    exp = mt.e**(a*x)
    exp2 = mt.e**(2*a*x)
    numerador1 = ( exp**2 ) * ( - ( (2*b*w**2)*sen ) - ( a*w*cos*exp ) + ( (w**2)*sen*exp ) + ( (a**2)*sen*exp ) + ( a*w*cos*exp ) )
    numerador2 = ( - (2*b*w*cos) + ( w*cos*exp ) - ( a*sen*exp ) ) * ( - ( 4*a*exp ) + ( 2*a*exp2 ) )
    numerador = numerador1 + numerador2
    denominador = ( 2 - (exp) )**4
    return numerador/denominador


# x = []
# y = []
# y2 = []
# y3 = []
# for j in arange(-100, 100, 1):
#     # print("x = {:<17f}) : f(x)= {:<17f} : f(x)= {:<17f} : f(x)= {:<17f}".format(j, funcr(j), func(j), 1) )
#     x.append(j)
#     y.append(funcr(j))
#     y2.append(func(j))
#     y3.append(funcl(j))

# plt.plot(x, y, 'r-')
# plt.plot(x,y2, 'g-')
# plt.plot(x,y3, 'b-')
# plt.ylabel('gráfico')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()

def bisseccao(a, b):
    i = 0
    precisao = 1e-3
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
    print("ponto na função: f({:^10.5f}) = {:>10.5f}".format(xzero, funcr(xzero)))
    if( funcl(xzero) < 0 ):
        print("é ponto de máximo\n")
    else:
        print("é ponto de minimo\n")
    return xzero

bisseccao(-100, 0)
bisseccao(0, 100)