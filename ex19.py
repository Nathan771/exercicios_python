sal = float(input("Quanto você ganha por horas trabalhadas? "))
horas = float(input("Quantas horas você trabalhou nesse respectivo mês? "))

total = sal*horas

descontos_imposto_renda = total * 0.11
descontos_inss = total * 0.08
descontos_sindicato = total * 0.05 

descontos_totais = (descontos_imposto_renda + descontos_inss + descontos_sindicato)

total_com_descontos = (total - descontos_totais)

print(f"O seu salário total com os descontos no referido mês é de R$ {total_com_descontos}")