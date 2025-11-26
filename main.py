from time import sleep

tabuada = 1

while True:
    print('=*' * 25)
    tabuada = int(input('Digite um número para saber a tabuada: '))
    print('=*' * 25)

    if tabuada <= 0:
        break

    print("\033[34mCarregando tabuada", end='')
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".\033[m")

    sleep(1.5)

    print('')

    t = 1
    while t < 11:
        print(f'{tabuada} X {t} = {t*tabuada} ')
        t = t + 1
        
print('Fim')
print('=*' * 25)
