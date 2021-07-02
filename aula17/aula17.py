"""
while
"""

# while True:
#     nome = input("Qual o seu nome? ")
#     print(f'Ola {nome}!')
#     break
#
# print('Não sera executada.')

# x = 0
# while x < 10:
#     print(x)
#     x = x + 1
#
# print('Acabou!')


while True:
    print()
    numb_1 = input('Digite um numero: ')
    numb_2 = input('Digite outro numero: ')
    operator = input('Digite um operador: ')

    if not numb_1.isnumeric() or not numb_2.isnumeric():
        print('Você precisa digitar um numero.')
        continue

    numb_1 = int(numb_1)
    numb_2 = int(numb_2)

    #+, -, /, *
    if operator == '+':
        print(numb_1 + numb_2)
        break
    elif operator == '-':
        print(numb_1 - numb_2)
        break
    elif operator == '/':
        print(numb_1 / numb_2)
        break
    elif operator == '*':
        print(numb_1 * numb_2)
        break
    else:
        print('Operador invalido!!')


















