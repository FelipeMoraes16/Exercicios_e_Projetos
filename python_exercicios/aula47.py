"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    entrada = input("Digite uma letra ou se quiser sair digite '0': ")

    if entrada == '0':
        break

    numero_tentativas += 1

    if len(entrada) > 1:
        print('Digite apenas uma letra.')
        continue

    if entrada in palavra_secreta:
        letras_acertadas += entrada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU ! PARABENS !')
        print('A palavra era:', palavra_secreta)
        print('Numero de tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0