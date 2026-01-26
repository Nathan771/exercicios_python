def validador_media():

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    media = ((nota1 + nota2) / 2)

    if media >= 6:
        print("Aprovado! ")
    elif media < 6:
        print("Reprovado! ")
    elif media == 10:
        print("Aprovado com distinção! ")

validador_media()