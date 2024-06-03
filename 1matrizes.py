import random

#exe1 e exe2 (valores pelo usuário de 0 a 20)
def matrize_mn(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = int(input(f"Informe o elemento {i},{j}: "))
            if elemento > 20:
                print("Valores acima de 20 não permitidos...")
                return None
            else:
                linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_M(matriz):
    for linha in matriz:
        print(linha)

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))
matriz = matrize_mn(linhas, colunas)
imprimir_M(matriz)

#usando randit (valores aleatórios de 0 a 20)

def matrize_mn(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = random.randint(0,20)
            print(f'O elemento {i+1},{j+1} da sua matriz é: {elemento}')
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimir_M(matriz):
    for linha in matriz:
        print(linha)

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))
matriz = matrize_mn(linhas, colunas)
imprimir_M(matriz)


