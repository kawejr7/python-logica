#TEORIA

'''#Fatiamento
frase[9] = V
frase[9:13] = Vide
frase[:5] = Curso
frase[15:] = Python
frase = 'Curso em Vídeo Python
frase[9::3] = V e P h

#Análise
len(frase) = 21 caracteres
frase.count('o') = 3 vezes aparece o 'o'
frase.count('o', 0, 13) = conta quantos 'o´ tem de 0 ate 13 excetuando  o 13
frase.find('deo') = onde encontrou o deo, nesse caso 11
frase.find('Android') = 0 ou -1 significa que não foi encontrado
'Curso' in frase = True

#Transformação
frase.replace('Python', 'Android') = substituir python por Android
frase.upper() = transforma em maiúsculo mantendo o que já era maiúscula
frase.lower() = transforma em minúsculo mantendo o que já era minúscula
frase.title() = transforma apenas as primeiras letras de cada palavra em maiúscula
frase.capitalize() = transforma todos os caracteres em minuscúla e apenas a orimeira letra fica maiúscula

frase
    Aprenda Python
frase.strip() = remove todos os espaços inúteis
Aprenda Python
frase.rstrip() = remove somente os último espaços (direita)
frase.lstrip() = remove somente os primeiros espaços (esquerda)

#Divisão
frase.split() = divide conforme os espaços (cada palavra fica dentro de uma lista)
'-'.join(frase) = põe um traço entre as palavras "-"
'''

#PRÁTICA

frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
frase = print(len(frase.replace('Python' , 'Android')))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print('Oi')

print('''Olá,xxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx''')

