total = int(input('Digite o valor total da compra:'))
pag = int(input('''Selecione o tipo de pagamento
1 = A vista no boleto com 10% de desconto;
2 = A vista no catão com 5% de desconto;
3 = Em até 2x no cartão sem acrecimo no valor; 
4 = Em 3x ou mais no cartão com 20% juros;'''))
if pag == 1:
    desc = total - (total * 0.10)
    print('Obrigado pela preferência, o valor a ser pago é de {:.2f} reias'.format(desc))
elif pag == 2:
    desc = total - (total * 0.05)
    print('Obrigado pela preferência, o valor a ser pago é de {:.2f} reais'.format(desc))
elif pag == 3:
    div = total / 2
    print('Obrigado pela preferência, o valor das parcelas seram de {:.2f} reais'.format(div))
else:
    qta = int(input('Em quantas vezes será pago:'))
    jur = total + (total * 0.20)
    totpa = jur / qta
    print('Obrigado pela preferência, o valor {:.2f} será pago em {:.0f} meses e tera o valor reajustado para {:.2f}'.format(total, qta, jur))
    print('O valor das parcelas será de {:.2f} reais por mês'.format(totpa))