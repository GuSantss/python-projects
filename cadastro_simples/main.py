"""
Projeto: Cadastro Simples
Autor: Gustavo Santos
Descrição: Sistema em Python para cadastrar usuários via terminal.
"""

maior = 0
mulheres = 0
maioridade = 0

while True:
    nome = str(input("Digite seu nome completo: ")) 
    idade = int(input("Digite sua idade: "))
    if idade >= 18: #se for maior ou igual a 18, entra para a variavel maior, somando 1
        maior += 1
        maioridade = maior
    sexo = str(input("Digite sua sexualidade: (H/M) ")).upper()
    if sexo == "M": #se o sexo for igual a M (mulher), entra para a variavel mulheres, somando 1
        mulheres += 1

    cadastro = str(input("Deseja continuar cadastrando? (S/N) ")).upper() #pergunta se quer continuar

    while cadastro == "S": #se a resposta for S (sim), ele repete todo o processo
        
        nome = str(input("Digite seu nome completo: "))
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            maior += 1
            maioridade = maior
        sexo = str(input("Digite sua sexualidade: (H/M) ")).upper()
        if sexo == "M":
            mulheres += 1

        cadastro = str(input("Deseja continuar cadastrando? (S/N) ")).upper()
    else:
        print("-=" * 25)
        print(f"Resumo de Cadastros".center(50))
        print(f"Maioridade: {maioridade}".center(50))
        print(f"Mulheres: {mulheres}".center(50))
        print("-=" * 25)
        break