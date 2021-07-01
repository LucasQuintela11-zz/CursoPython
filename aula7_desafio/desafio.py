"""
Criar variavies para nome (str), idade (int),
Criar altura(float), e peso(float) de uma pessoa
Criar variavel com ano atual (int)
Obter o ano de nascimento de pessoa (baseada na idade e no ano atual)
obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando f-string
"""

nome = 'Lucas'
idade = 24
altura = 1.80
peso = 96
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e tem {altura} de altura.')
print(f'{nome} tem {peso} kilos e seu imc e {imc:.2f}')