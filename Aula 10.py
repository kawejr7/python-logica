#TEÓRICA

#LISTA DE COMANDOS            C
#carro.siga()
#carro.esquerda()
#carro.siga
#carro.direita()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#FLUXO VERDE se carro.esquerda()
#FLUXO VERMELHO senão

#carro.siga() <SEMPRE ACONTECE
#se carro.esquerda() bloco_v_
#    '''carro.siga()
#   carro.direita()
#    carro.siga()
#   carro.direita
#    carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga'''
#senão  bloco_f_
   #carro.siga()
   #carro.esquerda()
   #carro.siga()
   #carro.esquerda()
   #carro.siga()
#carro.para() <SEMPRE ACONTECE

        #CONDIÇÃO#

#if carro.esquerda():
 #  bloco true
#else:
 #  bloco false

t = int(input('Quantos anos tem seu carro?'))
if t <=3:
    print('carro novo')
else:
    print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

#PRÁTICA

            #CONDIÇÃO SÍMPLES
n = str(input('Qual seu nome?'))
if n == 'Gustavo':
    print('Que nome lindo,')
else:
    print('Seu nome é feio')
print(f'Bom dia {n}!')

            #CONDIÇÃO COMPOSTA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m}')
if m >= 7:
    print('Aprovado, parabéns!')
else:
    print('Reprovado')

            #CONDIÇAO SIMPLIFICADA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m}')
print('Aprovado, parabéns!' if m >= 7 else 'Reprovado')