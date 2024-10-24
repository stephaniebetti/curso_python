adicao = 10 + 10
print('adicao', adicao)

subtracao = 10 - 5
print('subtracao', subtracao)

multiplicacao = 10 * 10
print('multiplicacao', multiplicacao)

divisao = 10 / 2.2
print('divisao', divisao)
# essa sempre retorna numeros float (decimais)

divisao_inteira = 10 // 2.2
print('divisao inteira', divisao_inteira)
# essa sempre retorna numeros int (inteiros)

exponenciacao = 2 ** 10
print('exponenciacao', exponenciacao)

modulo = 55 % 2 
print('modulo', modulo)
# resto da divisao

'''O que eh resto da divisao? Imagine uma conta de 
divisao da escola. Normalmente a esquerda voce vai
subtraindo os numeros para dividir, a sobra
ao finalizar a conta, eh o modulo aqui no python.

Eh como se eu estivesse perguntando? Quanto
sobra dessa divisao?'''

print(  ) 
# Mas porque eu ia querer saber o resto da divisao?
'''Exemplo: Como saber se um numero eh multiplo de outro?
voce pode descobrir atraves do modulo.'''

# Ex: 10 eh divisivel por 8?
'''se o retorno for 0, entao 10 eh divisivel por '''
print(10 % 8)
# terminal -> 2

''' Vamos checar em codigo ao inves de usar o terminal?'''
print(10 % 8 == 0)
# terminal -> false

'''continuando'''
print(16 % 8 == 0)
# terminal -> true

print(  ) 
'''como saber se um numero eh par ou impar?'''
# ele tem que ser divisivel por 2
print(10 % 2 == 0) # terminal -> true
print(15 % 2 == 0) # terminal -> false
print(16 % 2 == 0) # terminal -> true