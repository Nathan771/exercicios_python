peso = float(input("Digite o peso: "))


excesso = (peso-50)
multa = (peso*4)

if peso > 50:
    print(f"Limite de peso ultrapassado! Quantidade de peso excedido: {excesso:.2f} kg. Valor total de multa a pagar: R$ {multa:.2f}")    
else:
    print(f"Peso válido total: {peso}.")


