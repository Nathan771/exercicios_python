metros = float(input("Informe o tamanho da área a ser pintada: "))

area_total = (metros*3)

quant_latas = (area_total/18)

preco_total = (quant_latas*80)

print(f"A quantidade necessária de latas de tinta para pintar a área é: {quant_latas} e o preço total: R$ {preco_total}")

