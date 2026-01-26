sal = float(input("Quanto você ganha por horas trabalhadas? "))
horas = float(input("Quantas horas você trabalhou nesse respectivo mês? "))

#Partindo do pressuposto de trabalho por 8h.

total = (sal*horas)

print(f"O seu salário total no referido mês é de R$ {total:.2f}")
