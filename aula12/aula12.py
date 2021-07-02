usuario = input('Digite o seu usuario: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa de no minino 6 caracteres')
else:
    print('Você foi cadastrado no sistema')