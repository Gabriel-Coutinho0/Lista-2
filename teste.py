a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a + b > c and a + c >b and b + c >a:
    if a==b==c:
        print ('Você tem um triangulo equilátero')
    elif a!=b!=c:
        print ('Você tem um triangulo escaleno')
    else:
        print ('Você tem um triangulo isósceles')
else:
    print ('não é um trigangulo')
