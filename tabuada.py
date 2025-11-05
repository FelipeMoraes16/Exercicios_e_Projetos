numeros = range(0, 11)

while True:

    entrada = input(
        'Digite qual tabuada você quer saber '\
        'ou digite 0 para sair: '
        )
    multiplicador = 0
    resultado = 0

    if entrada == '0':
        print('Obrigado por usar esse programa')
        break

    if entrada.isdigit():
        multiplicador = int(entrada)

        for numero in numeros:
            resultado = multiplicador * numero
            print(f'{multiplicador} x {numero} = {resultado}')

    else:
        print('Você não digitou um número inteiro')

    