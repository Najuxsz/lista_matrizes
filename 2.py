#exe3

def matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            elemento = int(input(f"Informe o elemento {i},{j}: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_M(matriz):
    for linha in matriz:
        print(linha)

def soma_par(matriz):
    soma = 0
    for i in matriz:
        for j in i:
            if j %2==0:
                soma +=j
    return soma

#exe4

def somar_coluna(coluna, num_coluna, matriz):
    soma_coluna = 0
    coluna = coluna-1   #na computação começa em 0, mas dificilmente o usuário saberá disso, então subtraimos 1 para ficar igual
    if coluna<= num_coluna and coluna>=0:
        for i in matriz:
                soma_coluna+=i[coluna]
    elif coluna > num_coluna or coluna < num_coluna:
        print('Essa coluna não existe')
    return soma_coluna

#exe5
def maiorvalor_linha(linha, num_linhas, matriz):
    maior = 0
    linha = linha-1
    if linha<= num_linhas and linha>=0:
        for j in matriz[linha]:
            if j>maior:
                maior=j
    return maior


num_linhas = int(input("digite a qnt de linhas:\n"))
num_coluna = int(input("digite a qnt de colunas:\n"))
matriz = matriz(num_linhas,num_coluna)
imprimir_M(matriz)
print(f"A soma dos números pares da matriz são: {soma_par(matriz)}")
coluna = int(input("Qual coluna voce gostaria de somar?"))
print(f"A soma da coluna {coluna} é: ({somar_coluna(coluna, num_coluna, matriz)})")
linha = int(input("Qual linha você gostaria de pegar o mair valor?"))
print(f"O maior valor da linha {linha} é: ({maiorvalor_linha(linha, num_linhas,matriz)})")
