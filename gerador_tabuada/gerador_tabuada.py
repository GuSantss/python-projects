print("-=" * 25)
print("Gerador De Tabuada".center(50))
print("-=" * 25)

n = int(input("Digite um numero que queira a tabuada: "))

print("-=" * 25)
print(f"Tabuada do número {n}".center(50))
print("-=" * 25)
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

while True:
    continuar = str(input("Voce quer continuar? (S/N) ")).upper()
    if continuar == "S":
        
        n = int(input("Digite um numero que queira a tabuada: "))
        print("-=" * 25)
        print(f"Tabuada do número {n}".center(50))
        print("-=" * 25)

        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("Voce escolheu sair.")
        print("Saindo...")
        break
