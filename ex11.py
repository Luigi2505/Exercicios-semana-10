tamanho = int(input("Digite o tamanho dos vetores: "))

A = [0] * tamanho
B = [0] * tamanho
C = [0] * tamanho

for i in range(tamanho):
    A[i] = int(input(f"Digite o {i + 1}° número para o vetor A: "))
    i += 1

for i in range(tamanho):
    B[i] = int(input(f"Digite o {i + 1}° número para o vetor B: "))
    i += 1

for i in range(tamanho):
    C[i] = A[i] + B[i]
    i += 1

print(f"Vetor A: {A}")
print(f"Vetor B: {B}")
print(f"Vetor C (A+B): {C}")

