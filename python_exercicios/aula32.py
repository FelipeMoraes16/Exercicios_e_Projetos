"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# # entrada do usuário
# entrada = input('Digite um número inteiro: ')

# # verifica se o que foi digitado é um número inteiro
# e_um_numero = entrada.isdigit()

# # se for um número inteiro
# if e_um_numero:

#     numero_inteiro = int(entrada)# converte a entrada para int
#     e_par = numero_int % 2# pega o resto da divisão por 2

#     # se o resto da divisão for 0
#     if e_par == 0:
#         print('É número par')
#     # se o resto da divisão for outro valor
#     else:
#         print('É número ímpar')

# # se o que foi digitado não for um número inteiro
# else:
#     print('Não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Digite que horas são em formato de 0-23 horas: ')

# e_numero_inteiro = entrada.isdigit()

# if e_numero_inteiro:

#     numero_inteiro = int(entrada)
#     cedo = numero_inteiro >= 0 and numero_inteiro <= 11
#     tarde = numero_inteiro >= 12 and numero_inteiro <= 17
#     noite = numero_inteiro >= 18 and numero_inteiro <= 23
    
#     if cedo:
#         print('Bom dia')

#     if tarde:
#         print('Boa Tarde')

#     if noite:
#         print('Boa noite')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu primeiro nome: ')

digitou_alguma_coisa = entrada

if digitou_alguma_coisa :
    total_letras = len(entrada)

    curto = total_letras <= 4
    normal = total_letras >=5 and total_letras <= 6
    muito_grande = total_letras >= 7

    if curto:
        print('Seu nome é curto')

    if normal:
        print('Seu nome é normal')
    
    if muito_grande:
        print('Seu nome é muito grande')

else:
    print('Você não digitou nada')