numeros = [0] * 10
for i in range(10):
    numeros[i] = int(input(f"Insira o {i + 1}° número inteiro: "))

for i in range(9):
    menor = i
    for j in range(i + 1, 10):
        if numeros[j] < numeros[menor]:
            menor = j
    numeros[i], numeros[menor] = numeros[menor], numeros[i]
print(numeros)

