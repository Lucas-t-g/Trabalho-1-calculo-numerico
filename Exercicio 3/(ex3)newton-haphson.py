import math as mt
from time import sleep
from numpy import arange
import matplotlib.pyplot as plt

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



# x = []
# y = []
# y2 = []
# y3 = []
# for j in arange(0, 2.1, 0.001):
#     # print("x = {:<17f}) : f(x)= {:<17f} : f(x)= {:<17f} : f(x)= {:<17f}".format(j, funcr(j), func(j), 1) )
#     x.append(j)
#     y.append(funcx(j))
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

def new_haph( b):
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
    print("número de iterações: ", i)
    print("raiz aproximada: f({:<17}) = {:<17}".format(x2, func(x2)))
    print("ponto na função: f({:^17}) = {:>17}".format(x2, funcx(x2)))
    print("ponto na derivada segunda: f({:^17}) = {:>17}".format(x2, funcl(x2)))
    if( funcl(x2) < 0 ):
        print("é ponto de máximo\n")
    else:
        print("é ponto de minimo\n")
    return x2

new_haph(0)
new_haph(1.5)