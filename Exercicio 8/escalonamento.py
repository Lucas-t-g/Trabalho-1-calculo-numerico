import math as mt
def entrada():
	linhas = eval(input('informe o numero de linhas: '))
	colunas = eval(input('informe o numero de colunas: '))

	matriz = []
	cont_linhas = 1

	while cont_linhas <= linhas:
		Linha = []
		cont_colunas = 1
	
		while cont_colunas <= colunas:
			elemento = float(input('informe o elemento ('+str(cont_linhas)+','+str(cont_colunas)+'): '))
			Linha.append(elemento)
			cont_colunas += 1
		print("\n")
		matriz.append(Linha)
		cont_colunas = 1
		cont_linhas += 1
	return matriz,linhas,colunas
	
#para testar com outro metodo  de entrada(diretamente pelo codigo)
matriz = [[6.0, 2.0, -1.0, 7.0], [2.0, 4.0, 1.0, 7.0], [3.0, 2.0, 8.0, 13.0]]
linhas = 3
colunas = 4


def print_matriz(matriz):
	cont_print = 0
	while cont_print < linhas:
		print (matriz[cont_print])
		cont_print += 1


def linhas_nulas(matriz,linhas,colunas,cont0): #joga linhas nulas pro final da matriz
	cont_linha = 0
	matriz00 = []

	while cont_linha < len(matriz) :
		linha = matriz[cont_linha]
		cont_elem = 0
		num0 = 0
		while cont_elem < colunas:
			if linha[cont_elem] == 0:
				num0 += 1
			else:
				cont_elem = colunas
			cont_elem += 1
		if num0 == colunas:
			matriz00.append(linha)
			matriz.pop(cont_linha)
			cont0 += 1
			
		cont_linha += 1
	matriz = matriz + matriz00
	return matriz, cont0


def zero_zero(matriz,linhas,colunas):
	cont_linha = 0
	while cont_linha < linhas:
		 cont_coluna = 0
		 while cont_coluna < colunas:
		     if abs( matriz[cont_linha][cont_coluna] )< 0.0000000001:
		         matriz[cont_linha][cont_coluna]= 0.0
		     cont_coluna += 1
		 cont_linha += 1
	return matriz

# matriz, linhas, colunas = entrada()

print ('sua matriz:')
print_matriz(matriz)

matriz2 = [] #linhas q comecam com 1
matriz3 = [] #linhas q comecam com 0
cont = 0
cont1 = 0
cont0 = 0

matriz,cont0 = linhas_nulas(matriz,linhas,colunas,cont0)

for linha in matriz: #coloco em cima as matrizes q cmecam com '1' e em baixo as q comecam com 0
	if linha[0] == 1:
		matriz2.append(linha)
		matriz.pop(cont)
		cont1 += 1
	elif linha[0] == 0:
		matriz3.append(linha)
		matriz.pop(cont)
		cont0 += 1

	cont += 1


matriz4 = matriz 
matriz = matriz2 + matriz4 + matriz3

print("--------------------------------")
print_matriz(matriz)

coluna = 0
cont_linha = 0

def escal(matriz,cont1,cont0,coluna,cont_linha,linhas,colunas):
	cont = cont_linha
	while (cont < linhas)  : #transformo em '1' os elementos abaixo do pivo
	
		linha = matriz[cont]
		pivo = linha[coluna]
	
		cont_elem = 0
		if (linha[coluna] != 0):
			for elem in linha:
				linha[cont_elem] = elem/pivo #divide a linha pelo primeiro termo
				cont_elem += 1
		matriz[cont] = linha
		cont += 1

	cont = cont1
	prime = matriz[cont_linha]
	while (cont < linhas): #zera os elementos abaixo do pivo
		linha = matriz[cont]
		cont_elem = coluna
		

		if (linha[coluna] != 0):
			while cont_elem < colunas:

				linha[cont_elem] = linha[cont_elem] - prime[cont_elem]
				cont_elem += 1
		matriz[cont] = linha
		cont += 1
	cont1 += 1
	coluna += 1
	cont_linha += 1
	


	print("--------------------------------")

	print_matriz(matriz)
	#matriz = zero_zero(matriz,linhas,colunas)
	
	matriz, cont0 = linhas_nulas(matriz,linhas,colunas,cont0)
	
	return matriz, cont1, coluna, cont_linha



while coluna < colunas and cont_linha < linhas:

	matriz, cont1, coluna, cont_linha = escal(matriz, cont1, cont0, coluna, cont_linha,linhas, colunas)
	
	
	
#if linhas > colunas:
#    contF = linhas - 1
#    while contF > colunas:
#        elem_linha = matriz[contF]
#        for elem in elem_linha:
#            elem = 0.0
#        contFntF -= 1
		



		
		
print ('sua matriz escalonada:')
print_matriz(matriz)

print ("FIM!")
