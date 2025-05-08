vogal = 0
texto = input("Digite uma frase: ")
for i in texto:
    if i in "aeiou":
        vogal += 1
        print(i)
print(f"Vogais = {vogal}")









