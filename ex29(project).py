banco = []

def validate_user():
    while True: 
        user = input("Cadastre seu nome de usuário: ")
        password = input("Insira uma senha válida:")
        if user in banco:
            print("Usuário não disponível! ")
            continue
        else:
            banco.extend([user, password])
            print(banco)
            continue


validate_user()
   
def refresh_user()