#TEORIA

#outras possibilidades

#condicões aninhadas

'''carro.siga()
if carro.esquerda:                              #UM if
bloco 1
elif carro.direita:                             #QUANTOS elif QUISER
bloco 2
elif carro.ré:
bloco 3
else:                                           #NENHUM OU UM else
bloco 4'''

#PRÁTICA


n = str(input('QUal é seu nome? '))
if n == 'Kawe':                            #condição símples
    print(f'Que nome lindo, {n}')
print(f'Tenha um bom dia {n}!')




n = str(input('Qual é seu nome? '))
if n == 'Kawe':
    print('Que nome bonito!')
else:                                      #condição composta
    print('Nome sem graça!')
print(f'Tenha um bom dia {n}!')




n = str(input('Qual é seu nome? '))
if n == 'Kawe':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'maria' or n == 'Paulo':          #estrutura condicional aninhada
    print('Seu nome é popular no Brasil!')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Nome sem graça!')
print(f'Tenha um bom dia {n}!')
