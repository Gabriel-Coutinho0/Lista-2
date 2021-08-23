#cada 1 litro = 3 metros, cada lata tem 18 litros = 80 reais
#informe a quantidade de latas e o preço total
metros = float(input('Tamanho da area(metros quadrados): '))
if metros <= 18:
    print (f'Você precisa de 1 lata de tinta e vai custar: 80 ')
elif metros <=36:
    print (f'Você precisa de 1 lata de tinta e vai custar: {80 * 2} ')
