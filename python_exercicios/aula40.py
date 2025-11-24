# Calculadora com while

while True:

    entrada_numero1 = input('Digite um número: ')
    entrada_numero2 = input('Digite outro número: ')
    entrada_operador = input('Digite um operador (+-/*): ')

    numeros_validos = None
    numero1 = 0
    numero2 = 0

    try:
        numero1 = float(entrada_numero1)
        numero2 = float(entrada_numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    operadores_validos = '+-/*'

    if len(entrada_operador) > 1:
        print('Digite apenas um operador')
        continue

    if entrada_operador not in operadores_validos:
        print('Operador inválido')
        continue

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos')
        continue

    if entrada_operador == '+':
        print(f'{numero1} + {numero2} = ', numero1 + numero2)
    if entrada_operador == '-':
        print(f'{numero1} - {numero2} = ', numero1 - numero2)
    if entrada_operador == '/':
        if numero2 != 0:
            print(f'{numero1} / {numero2} = ', numero1 / numero2)
        else:
            print('Não da pra dividir por 0')
            continue
    if entrada_operador == '*':
        print(f'{numero1} * {numero2} = ', numero1 * numero2)

    sair = input('[s]air ? ').lower().startswith('s')

    if sair:
        break