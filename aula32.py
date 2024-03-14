"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero: ')

if numero.isdigit():
  int_numero = int(numero)
  if int_numero % 2 == 0:
    print('O número é par')
  else:
    print('O número é ímpar')
else:
  print('Não é um número inteiro')    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')

if hora.isdigit():
  int_hora = int(hora)
  if int_hora <= 11:
    print ('Bom dia')
  elif int_hora >= 12 and int_hora <=17:
    print ('Boa tarde')
  else: 
    print ('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
nome_curto = len(nome) <= 4
nome_medio = len(nome) >= 5 and len(nome) <= 6 

if nome_curto:
  print('Seu nome é curto')
elif nome_medio:
  print('Seu nome é normal')
else: 
  print('Seu nome é muito grande')

