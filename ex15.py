lista = []

for i in range(0,3):
    if i == 2:
        lista.append(float(input("Digite o valor decimal: ")))
    else:
        lista.append(int(input("Digite os valores inteiros: ")))

cal1 = ( (lista[0]*2) * (lista[1]/2))

print(f"Resultado: {cal1}")

cal2 = ((lista[0]*3) + lista[2])

print(f"Resultado da segunda operação: {cal2}")

cal3 = (lista[2]**3)

print(f"Resultado da terceira operação: {cal3} ")


