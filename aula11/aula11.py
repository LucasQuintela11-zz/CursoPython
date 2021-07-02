"""
Operadores Logicos - Aula 4
And, or, not
int e not in
"""

a = 2
b = 3

# if b > a:
#     print('B é maior do que A.')
# else:
#     print('A e mior do que B.')

# nome = 'Lucas Quintela'
#
# if 'u' in nome:
#     print('Existe a leta U no seu nome ')

usuario = input('Nome do usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'lucas'
senha_db = 'qwe123'

if usuario_bd == usuario and senha_db == senha:
    print('Você estal logado no sistema')
else:
    print('Usuario ou senha invalido')