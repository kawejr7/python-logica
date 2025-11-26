#             - - - - - M U N D O  2 - - - - -


#EXERCÍCIO 36


v = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual o seu salário? R$ '))
a = int(input('Em quantos anos pretende pagar? '))

p = (v / a) / 12

if s * 30 / 100 < p:
    print(f'Para pagar um empréstimo de R$\033[32m{v:.2f}\033[m em {a} anos\nA prestação será de R$\033[32m{p:.2f}\033[m\nO seu empréstimo foi  \033[31mnegado\033[m')
else:
    print(f'Para pagar um empréstimo de R$\033[32m{v:.2f}\033[m em {a} anos\nA prestação será de R$\033[32m{p:.2f}\033[m seu empréstimo foi \033[32maprovado!\033[m')


#EXERCÍCIO 37


n = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{n} convertido para  binário é igual a {bin(n)[2:]}')       #0b
elif opcao == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')      #0o
elif opcao == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')        #0x
else:
    print('Opção \033[31mINVÁLIDA\033[m')


#EXERCÍCIO 38


n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
if n1 > n2:
    print('o \033[34mprimeiro\033[m número é o maior.')
elif n1 == n2:
    print('\033[31mNão existe\033[m valor maior, os dois números são iguais')
else:
    print('O \033[33msegundo\033[m valor é o maior')


#EXERCÍCIO 39


from datetime import date
atual = date.today().year
a = int(input('Qual ano você nasceu? '))
i = atual - a
print(f'Quem nasceu em {a} tem {i} anos em {atual}')
if i < 18:
    print(f'Ainda faltam \033[34m{18 - i}\033[m anos para você se alistar.')
elif i == 18:
    print('Já está na hora de você se alistar no \033[32mExército\033[m \033[33mBrasileiro\033[m! Procure a junta militar mais próxima.')
else:
    print(f'Você deveria ter se alistado há \033[31m{i - 18}\033[m anos, procure uma \033[1mjunta militar\033[m.')



a = int(input('Qual sua idade? '))
i = 18
if a < 18:
    print(f'Ainda faltam \033[34m{i - a}\033[m anos para você se alistar.')
elif a == 18:
    print('Já está na hora de você se alistar no \033[32mExército\033[m \033[33mBrasileiro\033[m! Procure a junta militar mais próxima.')
else:
    print(f'Você deveria ter se alistado há \033[31m{a - i}\033[m anos, procure uma \033[1mjunta militar\033[m.')



#EXERCÍCIO 40


from time import sleep
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2

print('\033[36mCalculando...\033[m')
sleep(2)

if m < 5:
    print('\033[31mReprovado\033[m')
elif m == 5 and m < 7:
    print('\033[33mRecuperação\033[m')
elif m == 7 and m < 9:
    print('\033[32mAprovado\033[m')
elif m > 8.5:
    print('\033[32mAprovado!\033[m\n\033[34mParabéns\033[m pelo seu \033[36mdesempenho!!!\033[m')


#EXERCÍCIO 41



from datetime import date
atual = date.today().year

n = int(input('Ano de nascimento: '))
i = atual - n
print(f'O atleta tem {i} anos')

if i <= 9 :
    print('Categoria: \033[34mPré mirim\033[m')
elif i <= 14:
    print('Categoria: \033[36mInfantil\033[m')
elif i <= 19:
    print('Categoria: \033[37mJunior\033[m')
elif i <= 20:
    print('Categoria: \033[35mSenior\033[m')
else:
    print('Categoria: \033[31mMaster\033[m')


i = int(input('Digite sua idade: '))
if i <= 9:
    print('Categoria: \033[34mPré mirim\033[m')
elif 9 < i <= 14:
    print('Categoria: \033[36mInfantil\033[m')
elif 14 < i <= 19:
    print('Categoria: \033[37mJunior\033[m')
elif 19 < i <= 20:
    print('Categoria: \033[35mSenior\033[m')
else:
    print('Categoria: \033[31mMaster\033[m')


#EXERCÍCIO 42


from time import sleep
print('-*-' * 20)
r1 = float(input('Reta 1: '))
print('-*-' * 20)
r2 = float(input('Reta 2: '))
print('-*-' * 20)
r3 = float(input('Reta 3: '))
print('-*-' * 20)



if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('As retas formam um triângulo!\nVamos ver qual é:')

sleep(1)
print('\033[36mCarregando...\033[m')
sleep(3)
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('Essas retas não formam um triângulo')

elif r1 != r2 and r1 != r3 and r2 != r3:
    print('As retas formam um \033[32mtriângulo\033[m \033[35mescaleno\033[m')


if r1 == r2 == r3:
    print('As retas formam um \033[32mtriângulo\033[m \033[34mequilátero\033[m')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('As retas formam um \033[32mtriângulo\033[m \033[33misósceles\033[m')


#EXERCÍCIO 43


p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a ** 2)
print(f'IMC(Ìndice de Massa Corporal): \033[97m{imc:.1f}\033[m')
if imc < 18.5:
    print('\033[37mAbaixo\033[m\033[m do peso')
elif 18.5 <= imc < 25:
    print('Peso \033[32mideal\033[m')
elif imc < 30:
    print('\033[33mSobrepeso\033[m')
elif imc < 40:
    print('\033[35mObesidade\033[m')
elif imc >= 40:
    print('\033[31mObesidade mórbida\033[m')



#EXERCÍCIO 44


p = float(input('Preço da compra: '))
print('''FORMAS DE PAGAMENTO\n[ 1 ] á vista dinheiro/pix\n[ 2 ] á vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais''')
o = input('Escolha a forma de pagamento: ')

if o == '1':
    print(f'Sua compra de R${p:.2f} vai custar R${p - (p * 10 / 100):.2f} no final\n(10%OFF)')
elif o == '2':
    print(f'Sua compra de R${p:.2f} vai custar R${p - (p * 5 / 100):.2f} no final\n(5%OFF)')
elif o == '3':
    print(f'Sua compra de R${p:.2f} vai continuar custando R${p:.2f}')
elif o == '4':
    print(f'Sua compra de R${p:.2f} vai custar R${p + (p * 20 / 100):.2f} no final\n(20%juros)')


#EXERCÍCIO 45


from time import sleep
from random import choice

opcoes = 'pedra', 'papel', 'tesoura'
pc = choice(opcoes)                 #SORTEAR PEDRA PAPEL OU TESOURA
u = str(input('Você escolheu: ')).strip().lower()

print('\033[37mPedra\033[m, \033[97mpapel\033[m, \033[33mtesoura\033[m...')
sleep(3)

if u == pc:
    print(f'Empate...Eu também escolhi {u}!')
elif u == 'pedra' and pc == 'tesoura':
    print(f'Você escolheu pedra e eu tesoura... Parece que eu perdi')
elif u == 'papel' and pc == 'pedra':
    print('Você escolheu papel e eu pedra... Parece que eu perdi')
elif u == 'tesoura' and pc == 'papel':
    print('Você escolheu tesoura e eu papel... Parece que eu perdi')
else:
    print(f'Hahá, você perdeu!Eu escolhi: {pc}')

from random import randint
itens = ('pedra' , 'papel', 'tesoura')
pc = randint(0, 2)
print('''Suas ações:
[ 0 ] pedra
[ 1 ] papel
[ 3 ] tesoura''')
u = int(input('Qual é a sua jogada? '))
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[u]}')

if pc == 0:
    if u == 0:
        print('EMPATE')
    elif u == 1:
        print('JOGADOR VENCE')
    elif u == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:

    if u == 0:
        print('COMPUTADOR VENCE')
    elif u == 1:
        print('EMPATE')
    elif u == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:

    if u == 0:
        print('JOGADOR VENCE')
    elif u == 1:
        print('COMPUTADOR VENCE')
    elif u == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')


#EXERCÍCIO 46


from time import sleep
for c in range(10, 0-1, -1):
    sleep(1)
    print(c,'!')
print('\033[34mViva o ano novo!\033[m')


#EXERCÍCIO 47


for n in range(1, 50+1, 2):
    print(n, end=' ')
print('\nEsses são os números \033[33mpares\033[m de 0 a 50!')


'''for n in range(0-1, 50+1):
    if n % 2 == 0:
        print(n)
print('\nEsses são os números \033[33mpares\033[m de 0 a 50!')'''


#EXERCÍCIO 48


soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont += 1
        soma += numero
print(f'\nA soma de todos os {cont} valores é {soma}')


#EXERCÍCIO 49


n = int(input('Digite um número para sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c} = {n*c}')


#EXERCÍCIO 50


soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
        print('')
    else:
        print('\033[31mDesconsiderado\033[m')
print(f'Você informou {cont} números pares e sua soma foi de {soma}')



#EXERCÍCIO 51


print('=' *20)
print('10 TERMOS DE UMA PA')
print('=' *20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('Fim')




#EXERCÍCIO 52


numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {numero} foi divisivel \033[33m{total}\033[m vezes')
if total == 2:
    print(f'O número \033[32m{numero}\033[m é primo! ')
else:
    print(f'O número \033[31m{numero}\033[m não é um número primo ')


#EXERCÍCIO 53


from time import sleep
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[:: -1]
print(f'A frase {frase} de trás para frente fica {inverso}'
      f'\nE...')
sleep(3)
if inverso == junto:
    print(f'E \033[32mé\033[m um \033[33mpalíndromo\033[m!')
else:
    print(f'\033[31mNão\033[m é um \033[33mpalíndromo\033[m')


#EXERCÍCIO 54

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    ano = int(input(f'Em que a ano a {pessoas}° pessoa nasceu? '))
    idade = atual - ano

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas \033[32mmaiores\033[m de idade \n'
      f'E tivemos {totmenor} pessoas menores de idade')

#EXERCÍCIO 55


maior = 0
menor = 0
media = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    media = media + peso / 5
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} Kg')
print(f'O menor foi{menor}')
print(f'A média de peso é {media}')



#EXERCÍCIO 56


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'\033[32m----- {p}° PESSOA -----\033[m')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:(M/F) ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade é de {mediaidade:.0f} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')




#EXERCÍCIO 57


sexo = 'FfMm'
while sexo not in 'Ff' and sexo not in 'Mm':
    sexo = str(input('Sexo: ')).upper()
    if sexo not in 'Ff' and sexo not in 'Mm':
        print('Tente novamente')
print('Seu sexo é ', end= '')
if sexo == 'F':
    print('\033[35mfeminino\033[m')
if sexo == 'M':
        print('\033[34mmasculino\033[m')


sexo = str(input('Sexo:[M/F] ')).upper().strip()[0]
while sexo not in 'FM':
        sexo = str(input('Dados inválidos, tente novamente: ')).upper().strip()[0]
print('Sexo ', end= '')
if sexo == 'F':
    print('\033[35mfeminino\033[m registrado com sucesso.')
if sexo == 'M':
        print('\033[34mmasculino\033[m registrado com sucesso.')


#EXERCÍCIO 58


from random import randint

tentativas = 1
pc = randint(0, 10)
print('-*-' * 17)
print('Vou pensar em um número, tente adivinhar qual é! ')  #JOGADOR TENTA ADIVINHAR
print('-*-' * 17)
j = 99
while j != pc:
    j = int(input('Digite um número: '))
    if j > 10:
        print('\033[31mErro\033[m')
    if j != pc:
        tentativas += 1
        print('Tente novamente. ')
if tentativas > 1:
    print(f'Você tentou {tentativas} vezes')
else:
    print(f'Você tentou apenas {tentativas} vez e acertou!')
print(f'Realmente era {pc} o número que eu escolhi.')
if tentativas > 3:
    print(f'Até que enfim você acertou!\n'
          f'Depois de \033[31m{tentativas} tentativas\033[m...')


#EXERCÍCIO 59


from time import sleep
maior = 0
s = 0
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
while s != 5:
    print('\n[ 1 ] somar\n'
            '[ 2 ] multiplicar\n'
            '[ 3 ] maior\n'
            '[ 4 ] novos números\n'
            '[ 5 ] sair do programa\n')
    s = int(input('Digite um número do menu: '))
    if s == 1:
        print(f'\033[36mSomando...\033[m')
        sleep(0.8)
        print(f'{v1} + {v2} = ', end='')
        print(v1 + v2)

    if s == 2:
        print(f'\033[35mMultiplicando...\033[m')
        sleep(1.4)
        print(f'{v1} X {v2} = ', end='')
        print(v1 * v2)
    if s == 3:
        if v1 > v2:
            print('\033[32mPensando...\033[m')
            sleep(1)
            print(f'O maior número é {v1}')
        else:
            print('\033[32mPensando...\033[m')
            sleep(1)
            print(f'O maior número é {v2}')

    if s == 4:
            print('\033[33mReiniciando...\033[m')
            sleep(2)
            v1 = float(input('Digite um valor: '))
            v2 = float(input('Digite outro valor: '))
    if s == 0 or s > 5:
        sleep(0.9)
        print('\n\033[31m[     E\033[m ',end='  ')
        sleep(0.8)
        print(f'\033[31mR\033[m', end='   ')
        sleep(0.7)
        print(f'\033[31mR\033[m', end='   ')
        sleep(0.6)
        print(f'\033[31mO', end='     ]\033[m\n')
        sleep(1.4)
        print('\n\033[36mCarregando...\033[m')
        sleep(2.2)
sleep(1)
print('\n\033[31mEncerrado.\033[m')
sleep(1)


# EXERCÍCIO 60


from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O factorial de {n} é {f}')

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else f' = {f} \n',end='')
    f = f * c
    c = c - 1

print(f'O factorial de {n} é {f}')


# EXERCÍCIO 61


print('=' *70)
print('GERADOR DE PA')
print('=' *70)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
termo = primeiro
cont = 1
while cont <= 10 :
    print(termo, end=' -> ')
    termo = termo + razao
    cont = cont + 1

print('Fim')
print('=' *70)




# EXERCÍCIO 62


print('=' *70)
print('GERADOR DE PA')
print('=' *70)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('pausa')
    mais = int(input('Quantos termos você quer ver mais? '))
    print(f'Total de PA´s: {total}')
print('Fim')



# EXERCÍCIO 63


print('-' * 30)
print('Sequência de Fibonnaci ')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> fim')


# EXERCÍCIO 64


n = 0
digitados = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    if n != 999:
        digitados += 1
if n == 999:
    print(f'Foi digitado {digitados} ',end='')
    if digitados >= 2 and n == 999:
        print('números')
    if digitados < 2 and n == 999:
        print('número apenas')

print(f'E a soma entre eles foi de {soma - 999}')


# EXERCÍCIO 65


resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quantidade
print('Acabou')
print(f'você digitou {quantidade} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')


# EXERCÍCIO 66


n = s = 0
digitados = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
    digitados = digitados + 1
print(f'Foram digitados {digitados} números e a soma entre eles foi {s}')


# EXERCÍCIO 67


tabuada = 1

tabuada = 1
while True:
    print('=*' * 25)
    tabuada = int(input('Digite um número para saber a tabuada: '))
    print('=*' * 25)
    if tabuada <= 0:
        break
    t = 1
    while t < 11:
        print(f'{tabuada} X {t} = {t*tabuada} ')
        t = t + 1
print('Fim')
print('=*' * 25)


# EXERCÍCIO 68


from random import randint
print('*=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('*=' * 20)
v = 0
while True:
    jogador = int(input('Jogue um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU! ')
            v = v + 1
        else:
            print('VOCÊ PERDEU ')
            break
    elif tipo  == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU ')
            v = v + 1
        else:
            print('VOCÊ PERDEU ')
            break
print(f'Total de vitórias: {v}')



# EXERCÍCIO 69


count = counts = countm = 0
print('*=' * 15)
print('CADASTRE UMA PESSOA')
print('*=' * 15)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    if idade >= 18:
        count = count + 1
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        counts = counts + 1
    if sexo == 'F' and idade < 20:
        countm = countm + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        print('*=' * 15)
    if resp in 'N':
        break
print(f'\nSão {count} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {counts} homens ')
print(f'E {countm} mulheres com menos de 20 anos foram cadastradas.\n ')
print('\033[31mencerrado\033[m')

# EXERCÍCIO 70


soma = countmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto:R$ '))
    cont = cont + 1
    soma = soma + preco
    if preco > 1000:
        countmil = countmil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'\nO total gasto na compra foi de R${soma:.2f}')
print(f'Foram {countmil} produtos gastos acima de mil reais')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')
print('\n\033[31mEncerrado\033[m')


# EXERCÍCIO 71


print('==' * 15)
print('{:^30}'. format('BANCO'))
print('==' * 15)
valor = int(input('Qual valor você quer sacar?R$ '))
cedula = 50
totalcedula = 0

while True:
    if total >= cedula:
        total = total - cedula
        totalcedula = totalcedula + 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break