idades = [0] * 5
for i in range(5):
    idades[i] = int(input(f"Insira a {i + 1}° idade: "))
media = (idades[0] + idades[1] + idades[2] + idades[3] + idades[4]) / 5
print(media)
