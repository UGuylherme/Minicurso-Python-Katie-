espaco = float (input('Espaço (m): '))
tempo = float (input('Tempo (s): '))
velocidademedia = espaco / tempo
print('A velocidade média é:', velocidademedia, 'm/s')

aceleracao = (velocidademedia / tempo)
print('A aceleração é:', aceleracao, 'm/s²')