import os

dados = []
total = 0

def limpar_terminal():
    os.system('cls' if os.name == "nt" else "clear")

while True:
    limpar_terminal()
    produto = {}

    while True:
        produto["nome"] = input("Digite o nome do produto: ").strip()
        if produto["nome"] != "":
            break
        print("Erro: O nome do produto não pode ficar em branco. Tente novamente. \n")

    while True:
        try:
            produto["preco"] = float(input("Digite o preço do produto: R$"))
            if produto["preco"] >= 0:
                break
            else:
                print("Erro: O preço não pode ser negativo. \n")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números para o preço. \n")

    while True:
        try:
            produto["quantidade"] = int(input("Digite a quantidade: "))
            if produto["quantidade"] > 0:
                break
            else:
                print("Erro: A quantidade deve ser maior que zero. \n")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números para a quantidade. \n")   

    total += produto["preco"] * produto["quantidade"]
    dados.append(produto)

    while True:
        add = input("Deseja adicionar mais algum item? (S/N) ").strip().upper()
        if add in ["S", "N"]:
            break
        print("Resposta inválida! Digite apenas S para sim e N para não. \n")
    if add == "N":
        break

limpar_terminal()
print(f"O valor total da compra foi de {total:.2f}")

while True:
    print("Qual será a forma de pagamento? \n[1] Pix \n[2] Crédito \n[3] Débito")
    try:
        pagamento = int(input("Escolha sua opção: "))
        if pagamento in [1, 2, 3]:
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas o número da opção.\n")

if pagamento == 1:
    limpar_terminal()
    print("NOTA FISCAL \n")
    for p in dados:
        print(f"{p["nome"]} - R${p["preco"]:.2f} - Qtd: {p["quantidade"]}. \n")
    print(f"Forma de Pagamento: PIX")
    print(f"Total: R${total:.2f} \n")
    print("Volte sempre!!")

elif pagamento == 2:
    limpar_terminal()
    while True:
        try:
            parcela = int(input(f"Em quantas vezes você deseja parcelar o valor de R${total:.2f}? \n"))
            if parcela > 0:
                break
            print("Erro: O número de parcelas deve ser maior que zero.\n")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para as parcelas.\n")

    ntotal = total / parcela
    limpar_terminal()
    print("NOTA FISCAL \n")
    for p in dados:
        print(f"{p['nome']} - R${p['preco']:.2f} - Qtd: {p["quantidade"]} \n")
    print("Forma de Pagamento: CRÉDITO")
    print(f"Parcelado em: {parcela}x de R${ntotal:.2f}")
    print(f"Total: R${total:.2f} \n")
    print("Volte sempre!!")

elif pagamento == 3:
    limpar_terminal()
    print("NOTA FISCAL \n")
    for p in dados:
        print(f"{p['nome']} - R${p['preco']:.2f} - Qtd: {p['quantidade']}. \n")
    print("Forma de Pagamento: DÉBITO")
    print(f"Total: R${total:.2f} \n")
    print("Volte sempre!!")
