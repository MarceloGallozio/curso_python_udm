nome = input('Qual seu nome? ')
altura = float(input('Qual sua altura? '))
peso = int(input('Qual seu peso? '))
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)