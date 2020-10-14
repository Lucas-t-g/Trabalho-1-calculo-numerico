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

        while cont_linha < len(self.matriz) :
            linha = self.matriz[cont_linha]
            cont_elem = 0
            num0 = 0 # pra contar quantos zeros tem na linha
            while cont_elem < colunas:
                if linha[cont_elem] == 0:
                    num0 += 1
                else:
                    cont_elem = colunas
                cont_elem += 1
            if num0 == colunas:
                matriz00.append(linha)
                self.matriz.pop(cont_linha)
                # cont0 += 1
            else:
                cont_linha += 1
        self.matriz += matriz00
        self.num_linhas_nulas = len(matriz00)
    
    def zera_zeros(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                elem  =  self.matriz[i][j]
                if abs(elem) < 1e-10:
                    self.matriz[i][j] = 0

    def escalona(self):
        #transformo em '1' os elementos abaixo do pivo
        while self.esc_estagio < self.linhas - self.num_linhas_nulas:
            self.zera_zeros()
            self.linhas_nulas()
            if False:
                for i in range(self.esc_estagio, self.linhas):
                    pivo = self.matriz[i][self.esc_estagio]
                    if pivo != 0:
                        for j in range(self.esc_estagio, self.colunas):
                            self.matriz[i][j] = self.matriz[i][j]/pivo  #divide a linha pelo primeiro termo
            
            # self.print_matriz()

            #subtraio todas as linhas abaixo da linha em questão
            pivo = self.matriz[self.esc_estagio][self.esc_estagio]
            for i in range(self.esc_estagio+1, self.linhas):
                m = self.matriz[i][self.esc_estagio] / pivo
                self.ms.append(m)
                for j in range(self.esc_estagio, self.colunas):
                    self.matriz[i][j] -= self.matriz[self.esc_estagio][j]*m
            
            self.esc_estagio += 1

    def desmancha(self):
        if self.colunas > self.linhas:
            self.Y_matriz = []
            for i in range(self.linhas):
                self.Y_matriz.append( [self.matriz[i].pop(self.colunas-1)] )
            self.colunas -= 1
    
    def solucao_lu(self):
        self.desmancha()
        self.escalona()

        L = []
        for i in range(self.colunas):
            L.append([0]*self.linhas)
            L[i][i] = 1

        for i in range(1, self.linhas):
            # print("i", i)
            for j in range(0, i):
                # print(i, j)
                L[i][j] = self.ms[i+j-1]

        L = np.matrix(L)

        U = np.matrix(self.matriz)

        print("matriz L*U = A = \n", np.dot(L, U), "\n")
        
        L = np.linalg.inv(L)
        print("matriz L':\n", L, "\n")

        U = np.linalg.inv(U)
        print("matriz U':\n", U, "\n")

        print("matriz L'*U' = A = \n", np.dot(L, U), "\n")
        # self.X_matriz = np.dot(U, Y)

        # print("matriz U invertida:\n", U, "\n")
        # print("matriz L invertida:\n", L, "\n")

        # print("solução do sistema:")
        # print(self.X_matriz, "\n")

        
            




#__COMEÇA_AQUI_______________________________________________________________

#para testar com outro metodo  de entrada(diretamente pelo codigo)
# a = [[6.0, 2.0, -1.0, 7.0], [2.0, 4.0, 1.0, 7.0], [3.0, 2.0, 8.0, 13.0]]
# a = [[-4.0, -1.0, 2.0, 7.0], [1.0, 6.0, -1.0, -6.0], [4.0, -3.0, -13.0, 6.0]]
# a = [[5.0, -1.0, 3.0, 1.0], [2.0, -10.0, 1.0, -7.0], [1.0, -2.0, 6.0, 5.0]]
a = [[4.0, 1.0, -1.0], [-3.0, 6.0, 2.0], [1.0, -5.0, 7.0]]
matriz = a
linhas = 3
colunas = 3
matriz = Matriz(matriz, linhas, colunas)
print("sua matriz: ")
matriz.print_matriz()

matriz.solucao_lu()


# xxx = np.matrix([[26/111,-1/111,4/111],[23/222,29/222,-5/222],[3/74,7/74,9/74]])
# print(xxx)