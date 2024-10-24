'''ordem de precendencia das operacoes 
aritmeticas (o que sera executado primeiro):'''
# 1 -> (n + n)
# 2 -> ** 
# 3 -> * / // % 
# 4 -> + -

conta_1 = 1+1 ** 5 + 5 
print(conta_1)
# o resultado seria 1024 mas vai dar 7!

'''porque deu 7 no terminal?'''
# devido a ordem que esta a variavel
# 1 -> foi realizado o ** -> 1 ** 5
# 2 -> depois foi o 


'''para dar 1024 a variavel seria:'''
conta_1 = (1+1) ** (5 + 5)
print(conta_1)