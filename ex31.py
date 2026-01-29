def predict():
    pais_A = float(input("Informa o total da população A: ")) 
    taxa_cresciment_A = (input("Informe a taxa A: "))
    pais_B = float(input("Informa o total da população B: "))
    taxa_crescimento_B = (input("Informe a taxa B: "))
    anos = 0

    if taxa_cresciment_A.endswith('%') or taxa_crescimento_B.endswith('%'):
        taxa_cresciment_A = float(taxa_cresciment_A[:-1]) / 100
        taxa_crescimento_B = float(taxa_crescimento_B[:-1]) / 100

    while pais_A < pais_B:
        pais_A *= (1 + taxa_cresciment_A)
        pais_B *= (1 + taxa_crescimento_B)
        anos +=1
        continue

        
    print(f"São necessários {anos} anos para o pais A ultrapasse o B")      
predict()