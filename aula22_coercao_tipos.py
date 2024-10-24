'''Conversao (ou Coercao) de Tipos'''
#type convertion, typecasting, coercion
# eh o ato de converter um tipo em outro

'''tipos imutaveis e primitivos:'''
# str, int, float, bool 

print(1+1) # o python soma normalmente
# isso eh chamado de polimorfismo

print('a'+'b')
# o pyhton vai juntar (concatenar)

'''isso eh uma caracteristica exclusiva 
de linguagens dinamicas como python. Voce
passa 2 tipos para o interpretador e ele
sabe o que fazer a partir disso.'''

print(   ) 
# o que acontece se voce colocar numeros entre aspas?
# lembrando que isso eh uma caracteristica das strings
# print('1' + 1) = erro no terminal
# ele fala que so pode fazer com str (strings)
print(int('1'), type(int('1')))
# conversao ok -> terminal: 1 <class 'int'>
print(int('1')+1) # converter str em int

print(   ) 
# float
print(float('1.5')+1) # converter str em float
print(float('1')+1) # o resultado vai ser em decimal (c/ ponto)
print(type(float('1')+1)) # identificar a funcao no terminal

'''
# logica de parenteses:
O python vai executar de dentro para fora. Ou seja, 
primeiro os parenteses de dentro e depois os de fora
da funcao.
'''

print(   ) 
# bool (boolean)
print(bool('')) # uma string vazia eh considerada false
print(bool('   ')) # assim ela eh considerada true (c/ espaco)

print(   ) 
'''como converter numero em string?'''
# print(11+'b) -> assim da erro
print(str(11)+'b') # assim vai concatenar (juntar)
