peso_peixe = float(input('Peso:'))
if peso_peixe <=50:
    excesso = 0
    multa = 0
    print ('Você teve um excesso de:',excesso,'e uma multa de:',multa)
else:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print (f'Voce teve um excesso de: {excesso:.2f} e uma multa de: {multa:.2f}') 
