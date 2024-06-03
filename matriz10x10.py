#exe6

def gerar_matriz():
    linha = 10
    coluna = 10
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            if i<j:
                elemento=2*i+7*j
                linha.append(elemento)
            if i==j:
                elemento=3*i**2
                linha.append(elemento)
            if i>j:
                elemento=(4*(i**3))+(5*(j**2))
                linha.append(elemento)
        matriz.append(linha)
    return matriz


def imprimir_M(matriz):
    for i in matriz:
        print(i)

matriz = gerar_matriz()
imprimir_M(matriz)