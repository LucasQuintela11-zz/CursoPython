"""
Operadores Relacionais - aula4
== > >= < <= !=
"""

nome = input('Qual o seu nome?')
idade = input('Qual sua idade')

idade = int(idade)
idade_limite = 18

if idade > idade_limite:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo')


