nota = 0
media = 0

print("-=" * 25)
print("Colégio Estadual Emilio de Menezes".center(50))
print("-=" * 25)

for i in range(5): #repete a pergunta 5x
    nota = float(input("Digite sua nota: ")) #guarda o valor das notas digitadas
    media += nota / 5 #soma todas as notas digitadas e calcula a media
    soma = media

print("-=" * 25)


if media >= 6:
    print("Você foi aprovado, PARABENS!".center(50)) #verifica se a media foi maior ou igual a 6

elif media < 6 and media > 5:
    print("Você ficou de recuperação!".center(50)) #verifica se a media foi menor que 6 e maior que 5

else:
    print("Você foi reprovado!".center(50)) #verifica se a media foi menor que 5


print(f"Sua média foi de {soma:.2f}".center(50))
print("-=" * 25)