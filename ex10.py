vetor = [2, 4, 7, 2, 3, 3 ,1 ,0, 2 ,6]

mais_frequente = 0
maior_contagem = 0

for num1 in vetor:
    contagem = 0
    for num2 in vetor:
        if num1 == num2:
            contagem += 1
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = num1

print("Número que mais se repete:", mais_frequente)
