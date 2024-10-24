""" a funcao print eh usada para exibir algo na tela. E ela
recebe uma coisa chamada de: argumento. O argumento eh
uma coisa que voce passa a funcao ou metodos. Eles podem 
ser separados por virgulas. """

print(12,34)
# para otimizar, posso duplicar a linha com ctrl+c e ctrl+v
print(56,78) # argumento nao nomeado (apenas funcao e numero/palavra)

# um argumento nomeado seria assim:
print(12,34, sep ="-")
print(56,78, sep='-')

print(12,34, sep ="joao")
print(56,78, sep='joao')
# o argumento SEP significa separador

""" na programacao existem caracteres que nao estao sendo
exibidos, mas estao fazendo alguma coisa. """

# Exemplo com quebra de linha:
# no MAC eh LF e no windowns eh CRLF
# essa informacao eh exibida no rodape do vs code

'''
CRLF: carriage return line feed
LF: Line feed
'''
# caracteres que representam essa quebra de linha:
# \r\n -> CRLF (windowns)
# \n -> LF (MAC e Linux)

print(12,34, sep ="-", end='\r\n')
print(56,78, sep='-', end ='\n')

'''e se colocarmos ##?'''
print(12,34, sep ="-", end='##')
# o argumento END sempre vai para o final
print(12,34, sep ="-", end='\n ##')
