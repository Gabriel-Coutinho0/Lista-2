metros = int(input('Metros: '))
if metros % 54 == 0:
  latas = m / 54
else:
  latas = int(metros / 54) + 1

valor = latas * 80
print (f'Sera necessario {latas} latas')
print (f'Total: R$ {valor:.2f}')
