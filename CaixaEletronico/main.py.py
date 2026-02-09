while True:
    
    #le o valor digitado
    saque = int(input("Digite o valor o qual vai ser sacado: R$"))

    cinquenta = saque // 50 #quantidade de notas 
    restante = saque - (50 * cinquenta) #restantante
    restante1 = restante

    vinte = restante1 // 20 #quantidade de notas 
    restante2 = restante1 - (20 * vinte) #restante

    dez = restante2 // 10 #quantidade de notas 
    restante3 = restante2 - (10 * dez) #restante

    um = restante3 // 1 #quantidade de notas
    restante4 = restante3 - (1 * um) #restante
    break

print(f"Total de {cinquenta} cédulas de R$50,00")
print(f"Total de {vinte} cédulas de R$20,00")
print(f"Total de {dez} cédulas de R$10,00")
print(f"Total de {um} cédulas de R$1,00")