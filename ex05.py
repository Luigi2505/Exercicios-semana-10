par = 0
impar = 0
for i in range(10):
    num = int(input(f"Digite o {i + 1}° número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Pares: {par}")
print(f"Impares: {impar}")