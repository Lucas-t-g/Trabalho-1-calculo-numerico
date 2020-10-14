import numpy as np

class Matriz:
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
        self.X_matriz = []
        self.Y_matriz = []
        self.ms = []
        self.linhas = linhas
        self.colunas = colunas
        self.esc_estagio = 0
        self.num_linhas_nulas = 0

    def print_matriz(self):
        print("-------------------------------")
        _linha = ""
        for linha in self.matriz:
            for elem in linha:
                _linha += "{:>8.4f}".format(elem)
            _linha += "\n"
        print(_linha)
        print("-------------------------------")
    
    def linhas_nulas(self):
        cont_linha = 0
        matriz00 = []

    def desmancha(self):
        if self.colunas > self.linhas:
            self.Y_matriz = []
            for i in range(self.linhas):
                self.Y_matriz.append( [self.matriz[i].pop(self.colunas-1)] )
            self.colunas -= 1

    def gaussjacobi(self, precisao):
        print("\nmétodo de Gauss-Jacobi:")
        k = 0
        x0 = np.zeros(self.linhas)
        alf = np.zeros(self.linhas)
        for i in range(0, self.linhas):
            x0[i] = 0.5
            s = 0
            for j in range(self.colunas):
                if( i != j ):
                    s +=  abs(self.matriz[i][j])
            alf[i] = s/abs(self.matriz[i][i])

        x = np.zeros(self.linhas)
        if( max(alf) < 1 ):
            teste = precisao+1
            while( teste > precisao ):
                k += 1
                for i in range(self.linhas):
                    s = 0
                    for j in range(self.colunas):
                        if( i != j ):
                            s += self.matriz[i][j]*x0[j]
                    x[i] = (self.Y_matriz[i][0] - s)/self.matriz[i][i]

                teste = max(np.absolute(x-x0))
                x0 = x.copy()
            x.reshape(3, 1)

            print("numero de iterações: {}".format(k))
            print("solução: ")
            print(x)
        else:
            print("não converge")

    def gausssidel(self, precisao):
        print("\nmétodo de Gauss-Sidel:")
        k = 0
        x0 = np.zeros(self.linhas)
        bet = np.zeros(self.linhas)+1
        for i in range(0, self.linhas):
            x0[i] = 0.5
            s = 0
            for j in range(self.colunas):
                if i != j:
                    if j > i:
                        s +=  abs(self.matriz[i][j])
                    else:
                        s += bet[j]*abs(self.matriz[i][j])

            bet[i] = s/abs(self.matriz[i][i])

        x = np.zeros(self.linhas)
        if( max(bet) < 1 ):
            x = x0.copy()
            teste = precisao+1
            while( teste > precisao ):
                k += 1
                for i in range(self.linhas):
                    s = 0
                    for j in range(self.colunas):
                        if( i != j ):
                            s += self.matriz[i][j]*x[j]
                    x[i] = (self.Y_matriz[i][0] - s)/self.matriz[i][i]
                    
                teste = max(np.absolute(x-x0))
                x0 = x.copy()
            x.reshape(3, 1)

            
            print("\nmétodo de Gauss-Sidel")
            print("numero de iterações: {}".format(k))
            print("solução: ")
            print(x)
        else:
            print("não converge")



#__COMEÇA_AQUI_______________________________________________________________

#para testar com outro metodo  de entrada(diretamente pelo codigo)
# a = [[6.0, 2.0, -1.0, 7.0], [2.0, 4.0, 1.0, 7.0], [3.0, 2.0, 8.0, 13.0]]
# a = [[-4.0, -1.0, 2.0, 7.0], [1.0, 6.0, -1.0, -6.0], [4.0, -3.0, -13.0, 6.0]]
# a = [[5.0, -1.0, 3.0, 1.0], [2.0, -10.0, 1.0, -7.0], [1.0, -2.0, 6.0, 5.0]]
a = [[10.0, -1.0, 1.0, 1.0], [2.0, -8.0, -1.0, -7.0], [3.0, -4.0, 6.0, 5.0]]
a = [[23.0, -3.0, 4.0, 1.0], [1.0, 13.0, -3.0, 3.0], [1.0, 2.0, -2.0, -12.0]]
matriz = a
linhas = 3
colunas = 4
matriz = Matriz(matriz, linhas, colunas)
matriz.desmancha()
matriz.print_matriz()
print(matriz.Y_matriz)
matriz.gaussjacobi(1e-3)
matriz.gausssidel(1e-3)
