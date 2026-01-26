import time

lista = []

for i in range(0,4):
    nota = float(input(f"Digite a {i+1} nota "))
    lista.append(nota)

media = sum(lista) / len(lista)

print(f"A media das notas é {media}. ")

