nome = 'Lucas'
idade = 24
altura = 1.80
peso = 96
e_maior = idade > 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('E_amior:', e_maior)
imc = peso / altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:2f}')

