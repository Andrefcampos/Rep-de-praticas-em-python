'''Programa de aprovação de emprestimo para compra de imovel
- perguntar o valor da casa;
- o salário;
- numero de parcelas
- calcular o valor de prestação mensal (não exceder 30% do salário
 senão negar emprestimo)'''
print('Olá, iremos realizar algumas perguntas para finaciamento do seu imóvel.')
print('\33[1;33m-\33[m'*25)
print('Digite:\n\33[1;32m1 para continuar\33[m\n\33[1;31m2 para sair\33[m')
print('\33[1;33m-\33[m'*25)
opcao = int(input('Qual a opção desejada? '))
print('\33[1;33m-\33[m'*25)
if opcao == 1:
    casa = float(input('Qual o valor do imóvel a ser financiado? R$'))
    print('\33[1;33m-\33[m'*25)
    salario = float(input('Qual a sua renda mensal? R$'))
    print('\33[1;33m-\33[m' * 25)
    parcelas = int(input('Qual a quantidade de parcelas desejadas? '))
    print('\33[1;33m-\33[m' * 25)
    financiamento = casa / parcelas
    if financiamento <= salario*0.3:
        print('\33[1;44mPARABÉNS!!!\33[m\nSeu financiamento foi aprovado e o valor da parcela será \33[1;42mR${:.2f} em {}x\33[m.'.format(financiamento, parcelas))
    else:
        print('\33[1;41mQUE PENA!\33[m\nInfelizmente foi negado devido ao valor da parcela exceder o máximo de \33[1;31m30%\33[m da sua renda.'.format(financiamento))

else:
    print('\33[1;42mObrigado e volte sempre!\33[m')
