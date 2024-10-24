'''
Python = linguagem de programacao
Tipo de tipagem = dinamica / forte
str -> string -> texto
Strings sao textos que estao dentro de aspas
'''
# aspas simples
print('luiz otavio')

# aspas duplas
print("luiz otavio")
print("luiz otavio") # iniciar e fechar a str com o mesmo caractere
'''para pular para o proximo caractere, usar:'''
print("luiz \"otavio") # isso se chama escape

# escape
print("luiz \"otavio")
# aqui sera exibido as aspas antes do otavio
print("luiz \"otavio\"")
# assim o otavio fica entre 2 aspas

# r
print(r"luiz \"otavio\"")
# se colocar um r antes ele ira aparecer as barras

'''
Usar essas funcoes, apesar de uteis, torna o codigo
bastante poluido. Para representar de forma mais
limpa, posso utilizar:
'''
print('luiz "otavio"')
# usando aspas duplas dentro de aspas simples (:
print("luiz 'otavio'")
# usando aspas simples dentro de aspas duplas (:

'''Exercicio!'''
# como exibir explicito eh melhor que implicito:
print('explicito', 'eh', 'melhor-que-implicito', sep='-')
# como exibir simples eh melhor que complexo:
print('simples', 'eh', 'melhor-que-complexo', sep='-')


'''como transformar uma linha em codigo em comentario? 
Ao inves de ficar usando # ou aspas? '''
# escreva o codigo normalmente e depois selecione tudo
# use ctrl + barra
# o mesmo comando desfaz comentario e volta p/ codigo
