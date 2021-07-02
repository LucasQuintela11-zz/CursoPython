"""
Formatando os valores modificados

:s - Texto(strings)
:d - inteiros
:f - Numero de ponto flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ^) QUantidade (TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""
num_1 = 10
num_2 = 3

divisao = num_1 / num_2
print('{:.2f}'.format(divisao))


