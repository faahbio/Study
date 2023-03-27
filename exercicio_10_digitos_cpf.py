"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf_informado = input('Informe um CPF (somente números): ')
nove_digitos = cpf_informado[:9]

contador_1 = 10

resultado_1 = 0

for digito in nove_digitos:
    
    resultado_1 += int(digito) * contador_1
    contador_1 -= 1

primeiro_digito = (resultado_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(f'O primeiro dígito do CPF é: {primeiro_digito}')

dez_digitos = nove_digitos + str(primeiro_digito)

contador_2 = 11

resultado_2 = 0

for digito in dez_digitos:
    
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1

segundo_digito = (resultado_2 * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(f'O segundo dígito do CPF é: {segundo_digito}')