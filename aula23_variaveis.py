# introducao
'''Variaveis sao usadas para salvar algo na memoria do computador.'''

# PEP8: (pepi eiti)
'''inicie variaveis com letras minusculas, pode usar
numeros e underline_.'''

# O sinal de = eh o operador de atribuicao
'''ele eh usado para atribuir um valor a uma nome
(variavel).'''

# exemplo:
'''nome_variavel = expressao'''

# como utilizar, exemplo:
nome_completo = 'stephanie betti'
print(nome_completo)

# pode ser feito com numeros:
soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

# Como utilizar variaveis?
'''A ideia da variavel nao eh abreviar o codigo, 
e sim torna-lo mais legivel. Imagine que voce
precise repetir diversas vezes a mesma coisa em
um codigo, a variavel serve como um apoio para essa
situacao.'''

# relembrando a aula 22
print(int('1'), type(int('1')))
'''imagine utilizar essa funcao que foi feita na aula
22 varias vezes no codigo, para nao fazer isso
podemos criar uma variavel.'''

# utilizando variaveis, ficaria:
int_um = int('1')
print(int_um, type(int_um))
'''o terminal executou normalmente mostrando 
a classificacao: 1 <class 'int'>'''

# agora com bool (boolean)
int_um = bool('1')
print(int_um, type(int_um))
'''o terminal executou normalmente mostrando 
a classificacao: True <class 'bool'>'''

# importante !
'''A variavel precisa refletir exatamente o valor
dela. Voce e qualquer pessoa, precisa bater o olho
no seu codigo e saber exatamente a o que a variavel
se refere. Esse exemplo: int_um = bool('1') nao eh
uma boa variavel! Porque parece que se trata de
um numero inteiro e na verdade se trata de um bool.'''

# exemplo de uma boa variavel:
int_um = int('1')

# exercicio
nome = 'stephanie'
idade = 28
maior_de_idade = idade >= 18
# terminal alegou bool
# True <class 'bool'>

print('Nome:', nome)
# terminal -> Nome: stephanie

print('Nome:', nome, 'Idade:', idade)
# terminal -> Nome: stephanie Idade: 28

print('eh maior?', maior_de_idade)
# terminal -> eh maior? True