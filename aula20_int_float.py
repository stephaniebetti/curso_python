'''tipos int e float'''

# int -> numero inteiro
# o tipo int representa qualquer numero
# positivo ou negativo.
# int sem sinal eh considerado positivo.

# float -> numero com ponto flutuante
# o tipo float representa qualquer numero
# positivo ou negativo com ponto flutuante.
# float sem sinal eh considerado positivo.

''' a funcao type (tambem chamada de classe) 
mostra o tipo que o python inferiu ao valor.'''

# int
print(11)
print(-11)
print(0)

# float -> numero com casa decimal (sempre usar ponto)
print(1.1)
print(1.1, 10.11)
print(0.90)
print(0.00, -1.5)

# limpar o terminal
'''como transformar uma linha em codigo em comentario? 
Ao inves de ficar usando # ou aspas? '''
# escreva o codigo normalmente e depois selecione tudo
# use ctrl + barra
# o mesmo comando desfaz comentario e volta p/ codigo

print(   ) # pular linha no terminal

'''como descubrar se o numero eh int ou float?'''
print(type('otavio'))
# type vai te explicar  
# no terminal ele fala que eh uma string

print(type(1))
# no terminal ele fala que eh um int

print(type(0.5))
# no terminal ele fala que eh um float

print(type (1))
# no terminal ele fala que eh um int

print(type(1), type(-0.5), type(10), type(-2.5))
# <class 'int'> <class 'float'> <class 'int'> <class 'float'>
