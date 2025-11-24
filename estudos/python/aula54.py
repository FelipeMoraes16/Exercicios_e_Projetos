# lista de compras

import os

lista_compras = []

while True:

    opcao = input(
        'Selecione uma opção: \n'\
        '[i]nserir [a]pagar [l]istar [s]air: '
        )
    
    if opcao:
        os.system('cls')

    if opcao == 's':
        print('Saindo...')
        break
    
    elif opcao == 'i':
        valor = input('Valor: ')
        lista_compras.append(valor)

    elif opcao == 'a': 
        # if not lista_compras:
        #     print('Não foi possível apagar, a lista esta vazia')
        # else:
        #     indice_apagar = input('Digite o indice para apagar: ')

        #     if not indice_apagar.isdigit():
        #         print('Digite apenas números')
        #     else:
        #         indice_apagar_inteiro = int(indice_apagar)

        #         if indice_apagar_inteiro >= len(lista_compras):
        #             print('Não foi possível apagar, indice não existe')
        #         else:
        #             lista_compras.pop(indice_apagar_inteiro)
        indice_apagar = input('Digite o indice para apagar: ')

        try:
            indice_apagar_inteiro = int(indice_apagar)
            del lista_compras[indice_apagar_inteiro]
        except ValueError:
            print('Digite apenas números inteiros')
        except IndexError:
            print('Indíce não existe')
            
    elif opcao == 'l':
        if not lista_compras:
            print('A lista está vazia')
        else:
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
    
    else:
        print('Por favor digite "a", "i", "l" ou "s"')