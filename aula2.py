# \r\n -> CRLF
# \n -> \LF (ambos são quebradores de linha)
# sep= (separador)
# end= (coloca algo no final, normalmente a quebra de linha)

print(12, 34, 1011, sep='-', end="->")
print(56, 78, sep="-", end="\n") 
print(9, 10, sep="-", end="\n") 
