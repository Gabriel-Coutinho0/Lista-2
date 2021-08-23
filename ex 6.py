salario = float(input('Ganho por hora: '))
horas = float(input('horas trabalhadas: '))
salario_bruto = salario * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
desconto = ir + inss + sindicato
salario_liquido = salario_bruto - desconto
print (f'Salario bruto: {salario_bruto:.2f} , Salario liquido: {salario_liquido:.2f}')
print (f'Inss : {inss:.2f} , Sindicato: {sindicato:.2f}')
