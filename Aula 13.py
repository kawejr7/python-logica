    #TEORIA

#comando passo                 |
#comando passo                 |
#comando passo          #1 laço|
#comando passo                 |
#comando passo                 |


#destino pega

#1 -> 10

#Laço de repetição/

#laço c no intervalo(1,10)
#    passo
#pega

#em python:

#for c in range(1,10):
#    passo
#pega

#pular


    #passo
#pula           0->3
    #passo
#pula
    #passo
#pula

#laco c no intervalo(0,3)
#    passo
#    pula
#passo
#pega

#for c in range(0,3):
#    passo
#    pula
#passo
#pega

#for c in range(0,3):
#    if moeda:
#        pega
#    passo
#    pula
#passo
#pega

    #PRÁTICA


for c in range(1, 7):
    print('oi')
print('fim')

for c in range(0, 7, 2):
    print(c)
print('fim')


n = int(input('Digite um número'))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')


s = 0
for c in range(0, 3):
        n = int(input('Digite um valor: '))
        s += n
print(f'O somatório de todos os valores foi {s}')
