peso_peixe = float(input('Peso do peixe: '))
if peso_peixe > 50:
 valor_excesso = peso_peixe - 50
 valor_multa = valor_excesso * 4
 print (f'Você passou do peso limite, pague o valor de R$:{valor_multa:.2f} e o peso a mais é de:{valor_excesso:.2f} Kg')
elif peso_peixe <= 50:
 valor_excesso = 0
 valor_multa = 0
 print ('Você esta dentro do limte o valor a pagar sera R$:', valor_multa,'e o excesso é de:',valor_excesso, 'Kg')
 
