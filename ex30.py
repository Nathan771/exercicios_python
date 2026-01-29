def validate_info():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    salario = float(input("Digite o salário: "))
    est_civil = input("Informe o seu estado civil: ")

    while len (nome) > 3 and idade > 0 and idade < 150 and salario > 0 and est_civil.upper() == "s" or "c" or "v" or "d":
        print(f"Nome válido! ({nome}) \n Idade válida! ({idade}) \n Salário válido! \n ({salario:.4f}) Estado civil válido! ({est_civil})")
        break
validate_info()