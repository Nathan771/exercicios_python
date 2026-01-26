def vogalouconsoante():
    while True:
        question = input("Digite a letra: ").lower()

        if question in ("a", "e", "i", "o", "u"):
            print("É vogal! ")
            break
        elif question.isdigit():
            print("Letra inválida...")
            continue
        elif question not in ("a", "e", "i", "o", "u"):
            print("É consoante! ")
            break
            

vogalouconsoante()

