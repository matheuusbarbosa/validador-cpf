cpf = input('Digite um cpf: ')
qtd_caracteres = len(cpf)

if not cpf.isnumeric():
    print('CPF inválido! Digite apenas números.')

elif not qtd_caracteres == 11:
    print('CPF inválido! Quantidade inválida de caracteres.')


else:
    verifica_cpf = list(cpf[:9])
    resultado_cpf = cpf[9:]

dg_1, dg_2, dg_3, dg_4, dg_5, dg_6, dg_7, dg_8, dg_9 = verifica_cpf

vl_1 = int(dg_1) * 10
vl_2 = int(dg_2) * 9
vl_3 = int(dg_3) * 8
vl_4 = int(dg_4) * 7
vl_5 = int(dg_5) * 6
vl_6 = int(dg_6) * 5
vl_7 = int(dg_7) * 4
vl_8 = int(dg_8) * 3
vl_9 = int(dg_9) * 2

resultado1 = vl_1 + vl_2 + vl_3 + vl_4 + vl_5 + vl_6 + vl_7 + vl_8 + vl_9
primeiro_dg = 11 - (resultado1 % 11)

if primeiro_dg > 9:
    primeiro_dg = 0

vl_1 = int(dg_1) * 11
vl_2 = int(dg_2) * 10
vl_3 = int(dg_3) * 9
vl_4 = int(dg_4) * 8
vl_5 = int(dg_5) * 7
vl_6 = int(dg_6) * 6
vl_7 = int(dg_7) * 5
vl_8 = int(dg_8) * 4
vl_9 = int(dg_9) * 3
vl_10 = int(primeiro_dg) * 2

resultado2 = vl_1 + vl_2 + vl_3 + vl_4 + vl_5 + vl_6 + vl_7 + vl_8 + vl_9 + vl_10
segundo_dg = 11 - (resultado2 % 11)

novo_cpf = cpf[:9] + str(primeiro_dg) + str(segundo_dg)
if novo_cpf == cpf:
    print(f'O CPF {novo_cpf} foi validado com sucesso.')
else:
    print(f'O CPF {novo_cpf} é invalido.')