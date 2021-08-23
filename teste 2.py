a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a+b>c and a+c >b and b+c>a:
    if a==b==c:
        print ('Você tem um triangulo equilátero')
    elif a==b or a==c or b==c:
        print ('Você tem um triangulo isósceles')
    else:
        print ('Você tem um triangulo escaleno')
else:
    print ('Você não tem um triangulo')
    
