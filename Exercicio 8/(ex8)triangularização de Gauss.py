class Matriz:
    def __init__(self, matriz, linhas, colunas):
        self.matriz = matriz
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

            #subtraio todas as linhas abaixo da linha em questão
            pivo = self.matriz[self.esc_estagio][self.esc_estagio]
            for i in range(self.esc_estagio+1, self.linhas):
                m = self.matriz[i][self.esc_estagio] / pivo
                for j in range(self.esc_estagio, self.colunas):
                    self.matriz[i][j] -= self.matriz[self.esc_estagio][j]*m
            
            self.esc_estagio += 1
    
    def solucao_sistema(self):
        x = [1]*self.linhas
        # print(x)
        for i in range(self.esc_estagio-1, -1, -1):
            # print(" ")
            denominador = 0
            # print(self.esc_estagio-1, " -- ", self.colunas-1)
            for j in range(i, self.colunas-1):
                # print(j, self.matriz[i][j])
                denominador += self.matriz[i][j]*x[j]
            # print("den ",denominador, " !! piv: ", self.matriz[i][-1])
            x[i] = self.matriz[i][-1]/denominador
            # print(x)


        print("\nsolução do sistema:")
        for i in range(len(x)):
            print("x{} = {:>8.4f}".format(i, x[i]))
            




#__COMEÇA_AQUI_______________________________________________________________

#para testar com outro metodo  de entrada(diretamente pelo codigo)
# a = [[6.0, 2.0, -1.0, 7.0], [2.0, 4.0, 1.0, 7.0], [3.0, 2.0, 8.0, 13.0]]
a = [[-4.0, -1.0, 2.0, 7.0], [1.0, 6.0, -1.0, -6.0], [4.0, -3.0, -13.0, 6.0]]
# a = [[5.0, -1.0, 3.0, 1.0], [2.0, -10.0, 1.0, -7.0], [1.0, -2.0, 6.0, 5.0]]
matriz = a
linhas = 3
colunas = 4
matriz = Matriz(matriz, linhas, colunas)
print("sua matriz: ")
matriz.print_matriz()

matriz.escalona()

print("\nsua matriz triangularizada: ")
matriz.print_matriz()

matriz.solucao_sistema()