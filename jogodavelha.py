#3 linhas e 3 colunas     ---- ok
#imprimir o jogo   -------- ok
#de [0],[0] a [2],[2] ------- ok
#dois jogadores, ou apenas um? ----- ok
#valores a serem preenchidos e verificados 
#"matriz identidade" de X ou 0, encerra jogo = adicionar ponto jogador vencedor
#usar X e 0 ou 1 e 0?
#perguntar se deseja jogar novamente

import random

velha = [["","",""],
         ["","",""],
         ["","",""]
]

jogador = 2
jogadas = 0 
jogadas_Max = 9

def menu():
    global velha
    print(" 0       1       2")
    print("0 :" + velha[0][0] "  |   "  + velha[0][1] "   |   " + velha[0][2])
    print("-"*11)
    print("1 :" + velha[1][0] "  |   "  + velha[1][1] "   |   " + velha[1][2])
    print("-" *11)
    print("2 :" + velha[2][0] "  |   "  + velha[2][1] "   |   " + velha[2][2])
    print("-" *11)
    

def jogador_CPU():
    escolha = random.randint(0,1)

    
while True:
    menu()
    if jogador == 2 and jogadas<jogadas_Max:
        escolha_linha = int(input("Digite a linha desejada: {i}\n"))
        escolha_coluna = int(input("Digite a coluna desejada: {j}\n"))
        elemento = int(input("Você quer 1 ou 0?\n"))
        if elemento == 1:
            escolha_coluna and escolha_linha == elemento




