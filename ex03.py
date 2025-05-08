num = int(input("Digite um valor entre 1 e 10 para sua tabuada: "))
if num <= 10:
    for i in range(1, 11):
        resultado = num * i
        print(f"{i} x {num} = {resultado}")
else:
    print("Insira um número válido")