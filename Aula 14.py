# TEORIA

# enquanto nao maçã
    # se chao:
    #   passo
    # se buraco:
    #   pula
    # se moeda
    #   pega
# pega

# while not maçã:
#     if chao:
#         passo
#     if buraco:
#         pula
#      if moeda:
#         pula

#PRÁTICA

# for c in range(1,10):
#     print(c)
# print('fim')

# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print('fim')

# r = 'S'
# while r == 'S':
#     n = int(input('digite um número : '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números ímpares')