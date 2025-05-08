dentro = 0
fora = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}° número de 0 a 99: "))
    if num in range(10, 20):
        dentro += 1
    else:
        fora +=1
print(f"Dentro do intervalo [10,20]: {dentro}")
print(f"Fora do intervalo [10,20]: {fora}")
