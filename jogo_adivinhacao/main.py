"""
Projeto: Jogo de Adivinhação
Autor: Gustavo Santos
Descrição: Jogo em Python onde o usuário deve adivinhar um número gerado aleatoriamente pelo sistema.
"""


from random import randint

computador = randint(1, 10) #computador escolhe um numero aleatorio de 1 a 10
tentativa = 0 #começa com 0, pois nao houve tentativas

print("-=" * 25)
print("JOGO DE ADIVINHAÇÃO".center(50))
print("-=" * 25)

while True:
    jogador = int(input("Qual foi o número sorteado: ")) #primeira tentativa
    tentativa += 1 #caso erre, soma uma tentativa

    if jogador != computador: #se a sua resposta for diferente da sorteada, o looping começa novamente
        print("Você errou, tente novamente: ")
    elif jogador == computador: #se a sua resposta for igual a sorteada, voce ganha
        print("-=" * 25)
        print("Você acertou!".center(50))
        print(f"Foram necessaria {tentativa} tentativas, parabens!".center(50))
        print("-=" * 25)
        break