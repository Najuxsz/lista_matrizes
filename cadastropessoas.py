#exe7

'''matriz = [
    ["Nome", ""],
    ["CPF", ""],
    ["Idade", ""],
    ["Renda mensal", ""]
]

def cadastro_pessoas():
    for l,c in matriz:
        print(l + ":" + str(c))

def espaco(matriz):
    for i in range(4):
        for j in range(2):
            print(f'[{matriz[i][j]:^15}]', end ='')
        print()

def media_idade(matriz,cadastros_realizados):
    soma=0
    for i in matriz:
        soma+=matriz[2][1]
    media=soma/cadastros_realizados
    return media  

def media_renda(matriz,cadastros_realizados):
    soma=0
    for i in matriz:
        soma+=matriz[3][1]
    media=soma/cadastros_realizados   
    return media

def realizar_cadastro():
    nome = input("Digite seu nome: ")
    matriz[0][1] = nome 
    cpf = input("Digite seu CPF: ")
    matriz[1][1] = cpf 
    idade = int(input("Digite sua idade: "))
    matriz[2][1] = idade
    renda_mensal = float(input("Digite sua renda mensal: "))
    matriz[3][1] = renda_mensal

def imprimir_cadastros(matriz):
    for i in matriz:
        print(f"Nome: {matriz[0][1]}, CPF: {matriz[1][1]}, Idade: {matriz[2][1]}, Renda mensal: {matriz[3][1]}")

cadastros_realizados = 0
while True:
    print("Deseja fazer um cadastro?")
    print("1 - SIM")
    print("2 - NÃO")
    escolha = input("Digite: ")
    if escolha == "2":
        imprimir_cadastros(matriz)
        print(f"A média das idades é: {media_idade(matriz, cadastros_realizados)} ")
        print(f"A média das rendas mensais é: {media_renda(matriz, cadastros_realizados)} ")
        break       
    elif escolha == "1":
        realizar_cadastro()
        print('Pessoa cadastrada!')
        cadastros_realizados += 1
'''
def cadastro_pessoas():
    pessoas = []
    nome = str(input("Digite seu nome: "))
    pessoas.insert(0,nome) 
    cpf = int(input("Digite seu CPF: "))
    pessoas.insert(1,cpf) 
    idade = float(input("Digite sua idade: "))
    pessoas.insert(2,idade)
    renda_mensal = float(input("Digite sua renda mensal: "))
    pessoas.insert(3,renda_mensal)
    return pessoas

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
        
def media_idade(matriz,contador):
    soma = 0
    for i in matriz:
            soma+=i[2]
    media = soma/contador
    return media 

def media_renda(matriz,contador):
    soma = 0 
    for i in matriz:
            soma +=i[3]
    media = soma/contador
    return media 

cadastro = 0
matriz = []
while True:
    print("Deseja fazer um cadastro?")
    print("1 - Sim")
    print("2 - Ver pessoas cadastradas")
    print("3 - Sair")
    escolha = input("Digite: ")
    if escolha == "1":
        pessoa = cadastro_pessoas()
        matriz.append(pessoa)
        print("Pessoa adicionada!")
        cadastro +=1
    elif escolha == "2":
        print(f"A média das idades das pessoas cadastradas é: {media_idade(matriz,cadastro)}")
        print(f"A média da renda mensal dos cadastros é: {media_renda(matriz,cadastro)}")
        print("Pessoas cadastradas:")
        imprimir_matriz(matriz)
    elif escolha == "3":
        print("Encerrando...")
        break



