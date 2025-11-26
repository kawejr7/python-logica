#                    - - - - - M U N D O  1 - - - - -

#                                    ,_______________________,
#exemplos:                           | Ordem de precedência  |
#[1]                                 |                       |
#5+2==7    5**2==25                  |1 ()                   |
#5-2==3    5//2==2      5|_2         |2 **                   |
#5*2== 10  5%2==0,5     1| 2         |3 * / // %             |
#5/2==2,5                            |4 + -                  |
#[2]                                 L_______________________|
#5+3*2==11
#3*5+4**2==31
#3*(5+4)**2==243
#[3]
#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#s = n1 + n2
#m = n1 * n2
#d = n2 / n2
#i = n1 // n2
#p = n1 ** n2
#print(f'A soma vale {s} \na multiplicação {m} \ne a divisão é {d:}\n ')
#print(f'Divisão inteira {i} \ne potência {p} \n')

"""                                                              M U N D O - 1                                                                   """

#EXERCÍCIO 5


x = int(input('Um número:'))
print(f'O sucessor de \033[34m{x}\033[m é \033[32m{x+1}\033[m e o seu antecessor é\033[31m{x-1}\033[m')


#EXERCÍCIO 6


n = int(input('Um número: '))
print(f'O dobro de \033[97m{n}\033[m é \033[35m{n*2}\033[m, seu triplo \033[31m{n*3}\033[m e sua raiz quadrada é \033[36m{n * n}\033[m.')


#EXERCÍCIO 7


n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

if n1 + n2 < 14.0:

    print(f'Média final: \033[31m{(n1 + n2) / 2:.1f}\033[m\nVocê \033[31mreprovou\033[m\n\n\033[1mProcure seu professor para ver se há possibilidade de recuperaçâo\033[m')          # :.1f PARA LIMITAR CASA DECIMAL A 1 APÓS VÍRGULA!

elif n1 + n2 == 14.0:
    print(f"Média final: \033[33m{(n1 + n2) / 2:.1f}\033[m\n\033[33mVocê passou!\nMas foi por pouco,lembre-se de estudar mais. \033[m")

else:

    print(f"Média final: \033[32m{(n1 + n2) / 2:.1f}\033[m\nVocê \033[32mpassou!\033[m\n\033[36mParabéns!!!\033[m")


#EXERCÍCIO 8


x = float(input('Valor em metros: '))

km = x / 1000
hc = x / 100
dc = x / 10
dci = x * 10
c = x * 100
mm = x * 1000
print(f'O valor de {x:.0f} \033[97mmetros\033[m é:\nem \033[35mKM\033[m: {km:.1f}\nem \033[31mHC\033[m: {hc:.0f}\nem \033[33mdc\033[m: {dc:.0f}\nem \033[32mdci\033[m: {dci:.0f}\nem \033[37mcm\033[m: {c:.0f}\ne em \033[36mmm\033[m: {mm:.0f}\n')

print(f'O valor em \033[37mcentimetros\033[m de {x} \033[97mmetros\033[m é {x*100} já em \033[36mmilimetros\033[m é {x*1000}')


#EXERCÍCIO 9


n = int(input('Escolha um número(tabuada): '))
if n < 5:
    print(f'\033[1mTABUADA\033[m DO \033[31m{n}:\033[m ')
    print('-' * 12)
    print(f'{n} x {1:2} = {n*1} \n{n} x {2:2} = {n*2} \n{n} x {3:2} = {n*3} \n{n} x {4:2} = {n*4} \n{n} x {5:2} = {n*5} \n{n} x {6:2} = {n*6} \n{n} x {7:2} = {n*7} \n{n} x {8:2} = {n*8} \n{n} x {9:2} = {n*9} \n{n} x 10 = {n*10}')
    print('-' * 12)
else:
    print(f'\033[1mTABUADA\033[m DO \033[32m{n}:\033[m ')
    print('-' * 12)
    print(f'{n} x {1:2} = {n*1} \n{n} x {2:2} = {n*2} \n{n} x {3:2} = {n*3} \n{n} x {4:2} = {n*4} \n{n} x {5:2} = {n*5} \n{n} x {6:2} = {n*6} \n{n} x {7:2} = {n*7} \n{n} x {8:2} = {n*8} \n{n} x {9:2} = {n*9} \n{n} x 10 = {n*10}')
    print('-' * 12)


#EXERCÍCIO 10


x = float(input('digite quantos reais você tem: R$ '))
y = x / 5.50
print(f'Com R$\033[32m{x:.2f}\033[m\033[m você pode converter para U$\033[32m{y:.2f}\033[m.')


#EXERCÍCIO 11


x = float(input('Altura(m): '))
y = float(input('Largura(m): '))
a = x * y
print(f'Sua parede tem a \033[33mdimensão\033[m de {x}x{y}\nSua \033[31márea\033[m é de {a} \033[97mm²\033[m\n')
l = a / 2
print(f'A quantidade de \033[37mtinta\033[m para pintar uma \033[31márea\033[m de {a} \033[97mmetros\033[m, em \033[37mlitro\033[m é de {l} \033[37ml\033[m')


#EXERCÍCIO 12


x = float(input('Preço atual:R$ '))
y = x - (x * 5 / 100)
print(f'Preço promocional: {y} \033[32m(5%OFF)\033[m')


#EXERCÍCIO 13


s = float(input('Salário do funcionário: R$'))
y = s + (s * 15 / 100)
print(f'Salário com aumento em \033[35m15%\033[m: R$\033[32m{y:.2f}\033[m')


#EXERCÍCIO 14


c = float(input('informe a temperatura em °C:'))
f = 9 * c / 5 + 32
print(f'A temperatura em \033[33m{c}°C\033[m corresponde a \033[31m{f}°F\033[m')


#EXERCÍCIO 15


x = int(input('Informe quantos dias o carro foi alugado: '))
print(f'O carro foi alugado por {x} \033[34mdias\033[m')
d = x * 60              #R$60.0 por dia de carro alugado

y = float(input('Informe quantos KM foram rodados com o carro: '))
print(f'Foram rodados {y:.1f} \033[36mquilometros\033[m')
k = y * 0.15            #R$0.15 por km rodado

print(f'O custo total por \033[34mdias\033[m alugados foi de R$\033[32m{d:.2f}\033[m')

print(f'E o custo total pelos \033[36mquilometros\033[m rodados foi de R$\033[32m{k:.2f}\033[m ')
t = k + d
print(f'O custo final foi de: R$\033[32m{d + k}\033[m')

print(f'Totalizando assim:R${t:.2f}')


#EXERCÍCIO 16


#from math import trunc
#n1 = float(input('Digite um número: '))
#print(f'O número {n1} tem a parte inteira {trunc(n1)}')

n = float(input('Digite um valor: '))
print(f'O número {n} tem a parte inteira {int(n)}')


#EXERCÍCIO 17


from math import hypot
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjascente: '))
h = hypot(x, y)
print(f'A hipotenusa medirá: {h:.2f}')

#import math
#x = float(input('Digite o valor do cateto oposto: '))
#y = float(input('Digite o valor d cateto adjascente: '))
#h = math.hypot(x, y)
#print(f'A hipotenusa medirá: {h:.2f}')

'''x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor d cateto adjascente: '))
h = (x**2 + y**2) ** (1/2)
print(f'A hipotenusa medirá: {h:.2f}')'''

#EXERCÍCIO 18

''' import math
an = float(input('Digite um ângulo: '))
se = math.sin(math.radians(an))
print(f'O ângulo de {an} tem o seno de: {se:.2f}')
co = math.cos(math.radians(an))
print(f'O ângulo de {an} tem o cooseno de: {co:.2f}')
tan = math.tan(math.radians(an))
print(f'O ângulo de: {an} tem a tangente de {tan:.2f} ') '''



from math import radians, sin, cos ,tan
an = float(input('Digite o valor do ângulo: '))
se = sin(radians(an))
print(f'O ângulo de {an} tem seno de: {se:.2f}')
co = cos(radians(an))
print(f'O ângulo de {an} tem o cosseno de: {co:.2f} ')
tan = tan(radians(an))
print(f'O ângulo de {an} tem a tengente de: {tan:.2f} ')

#EXERCÍCIO 19

'''import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Qerceiro aluno: '))
l = [a1, a2, a3, a4]
random.shuffle(l)
print('A ordem de apresentação será: ')
print(l)'''

#EXERCÍCIO 20

from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceito aluno: '))
a4 = str(input('Quarto aluno: '))
l = [a1, a2, a3, a4]
shuffle(l)
print(f'A rodem de apresentação será: ')
print(l)

'''inport random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Qerceiro aluno: '))
l = [a1, a2, a3, a4]
random.shuffle(l)
print('A ordem de apresentação será: ')
print(l)'''

#EXERCÍCIO 21

import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('matue.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
        time.sleep(1)  #evita loop travando a CPU

print('Terminou de tocar')

print('O programa continua rodando enquanto a música toca')

'''pygame.init()
pygame.mixer.music.load('Ex 21.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)'''

#EXERCÍCIO 22
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome ao todo tem: {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem: {(nome.find(' '))} letras')
separa = nome.split()
print(separa)
print(f'Seu primeiro nome tem: {len(separa[0])} letras')
#EXERCÍCIO 23

n = int(input('Digite um número: '))
print(f'Unidade {n // 1 % 10}')
print(f'Dezena {n // 10 % 10}')
print(f'Centena {n // 100 % 10}')
print(f'Milhar {n // 1000 % 10}')

#EXERCÍCIO 24

c = str(input('Em qual cidade você nasceu? ')).strip().upper()
print(c[:6] == 'SANTO')

#EXERCÍCIO 25

frase = str(input('Nome completo: ')).strip().upper()
print('Seu nome tem Silva? ')
print('SILVA' in frase)


#EXERCÍCIO 26

frase = str(input('Nome completo: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')}')
print(f'A primeira letra A apareceu na posição {frase.find('A') +1}')
print(f'A última letra A apareceu na posição {frase.rfind('A') +1} ')


#EXERCÍCIO 27

n = str(input('Digite seu nome completo: ')).strip()
print(f'Muito prazer em te conhecer {n}')
n = n.split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')

#EXERCÍCIO 28

from random import randint
from time import sleep
pc = randint(0, 5)   #FAZ O COMPUTADOR SORTEAR UM NÚMERO DE 0 A 5
print('-*-' * 17)
print('Vou pensar em um número, tente adivinhar qual é! ')  #JOGADOR TENTA ADIVINHAR
print('-*-' * 17)

n = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(3)    #DELAY PARA ATRASAR O RESULTADO E DAR UM SUSPENSE

if n == pc:
    print(f'Você acertou! eu realmente pensei no número {n}')
else:
    print(f'Você errou! eu pensei no número {pc}')


#EXERCÍCIO 29

v = float(input(f'Velocidade do carro: '))

if v > 80:
    print(f'Você receberá uma multa no valor de: R${(v - 80) * 7:.2f} por exceder a velocidade máxima da via que é 80Km/h')
else:
    print('Tenha um bom dia e dirija com segurança')

#EXERCÍCIO 30

n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')

#EXERCÍCIO 31

from time import sleep
d = float(input('Qual a distancia da sua viagem?'))
print('PROCESSANDO...')
sleep(3)
if d <= 200:
    print(f'Você pagará R${d * 0.50:.2f} pela sua viagem de {d:.0f}Km')
else:
    print(f'Você pagará R${d * 0.45:.2f} pela sua viagem de {d:.0f}Km')

'''d = float(input('Qual a distancia da sua viagem?'))
p = d * 0.50 if d <= 200 else d * 0.45
print(f'Você pagará R${p:.2f} pela sua viagem de {d:.0f} Km')'''

#EXERCÍCIO 32

b: int = int(input('Ano: Coloque 0 para analisar o ano atual: '))
if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
    print(f'O ano de {b} é bissexto')
else:
    print(f'O ano de {b} não é bissexto')

#EXERCÍCIO 33

x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))


menor = z
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
print(f'O menor número foi {menor}' )

maior = z
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
print(f'O maior número foi {maior}')

#EXERCÍCIO 34
from time import sleep

s = float(input('Qual é o salário do seu funcionário? '))

print('Carregando...')
sleep(1)

if s <= 1250:
    print(f'O salário foi aumentado para R${s + (s * 15 / 100)}')
else:
    print(f'O salário foi aumentado para R${s + (s * 10 / 100)}')

#EXERCÍCIO 35

from time import sleep
print('-*-' * 20)
r1 = float(input('Reta 1: '))
print('-*-' * 20)
r2 = float(input('Reta 2: '))
print('-*-' * 20)
r3 = float(input('Reta 3: '))
print('-*-' * 20)

sleep(1)

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')



#CORES NO TERMINAL#

print('\033[31mOlá mundo') #letra vermelha
print('\033[31;43mOlá mundo') #letra vermelha e fundo amarelo
print('\033[1;31;43mOlá mundo') #em negrito a letra vermelha e fundo amarelo
print('\033[1;31;43mOlá mundo\033[m') #em negrito a letra vermelha e fundo amarelo indo até a frase
print('\033[4;97;45mOlá mundo\033[m') #sublinhado a letra branca e fundo roxo
print('\033[7;97;mOlá mundo\033[m')  #inverte o fundo e o texto
print('\033[0;33;44mOlá mundo\033[m') #fonte padrão letra amarela e fundo azul
print('\033[7;33;44mOlá mundo\033[m') #inverte texto e fundo

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')

nome = 'Guanabara'
print(f'Muito prazer em te conhecer, \033[4;34m{nome}\033[4;34m')