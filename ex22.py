import time

def escolha_genero():
    while True:
        quest_1 = str(input("Informe o gênero: ")).strip().lower()
        
        if quest_1 in ["f", "feminino"]:
            print("Sexo feminino escolhido! ")
            break 

        elif quest_1 in ["m", "masculino"]:
            print("Sexo masculino escolhido")
            break   

        else:
            print("Gênero inválido! ")
            time.sleep(2)
            continue
    
escolha_genero()