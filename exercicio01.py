'''FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR, O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER E
NO FIM DEVE MOSTRAR O TOTAL DE VITÓRIAS CONSECULTIVAS QUE ELE CONQUISTOU.'''


from random import randint
print('=-' * 20)
print('\033[1;33mVamos jogar PAR OU ÍMPAR?\033[m')
print('=-' * 20)
v = 0
while True:
    num = int(input('Escolha um valor:'))
    jogador = str(input('Par ou ímpar? [P/I]')) .upper() .strip()
    computador = randint(0,5)
    print(f'Eu escolhi {computador}!')
    soma = computador + num
    print(f'\033[1;32mA soma deu {soma}!\033[m')
    if jogador == 'P':
        if soma % 2 == 0:
            print('PARABÉNS,DEU PAR, VOCÊ GANHOU!!!')
            v += 1
        else:
            print('DEU ÍMPAR, EU GANHEI!!!')
            break
    if jogador == 'I':
        if soma % 2 == 1:
            print('PARABÉNS, DEU ÍMPAR,  VOCÊ GANHOU!!!')
            v += 1
        else: #se o resultado da soma der par
            print('DEU PAR, EU GANHEI!!!')
            break
print(f'FINISH!!! Você teve {v} vitórias!!!')