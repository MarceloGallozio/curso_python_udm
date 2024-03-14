"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]  i = inicio / f = final / p = passo
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:7])
print(len(variavel))
print(variavel[0:9:2])
print(variavel[::-1])