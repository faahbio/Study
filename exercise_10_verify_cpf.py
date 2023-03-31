# Verify CPF (Brazilian ID)
# Code in Portuguese

import re
import sys

while True:

    cpf_informado = input('Informe um CPF: ')

    cpf_num = re.sub(r'[^0-9]', '', cpf_informado)

    sequencial = cpf_informado == (cpf_informado[0] * len(cpf_informado))

    if sequencial:

        print('CPF inválido, repetição detectada')
        sys.exit()

    nove_digitos = cpf_num[:9]

    contador_1 = 10

    resultado_1 = 0

    for digito in nove_digitos:

        resultado_1 += int(digito) * contador_1
        contador_1 -= 1

    primeiro_digito = (resultado_1 * 10) % 11

    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    dez_digitos = nove_digitos + str(primeiro_digito)

    contador_2 = 11

    resultado_2 = 0

    for digito in dez_digitos:

        resultado_2 += int(digito) * contador_2
        contador_2 -= 1

    segundo_digito = (resultado_2 * 10) % 11

    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    if (primeiro_digito == int(cpf_num[-2])) and (segundo_digito == int(cpf_num[-1])):

        print('CPF válido')

    else:

        print('CPF inválido')
