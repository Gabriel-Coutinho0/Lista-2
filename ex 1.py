a = int(input('Lado A: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a + b > c and a + c >b and b + c >a:
   if a==b==c:
    print ('Você tem um triangulo equilátero')
   elif a!=b==c:
    print ('Você tem um triangulo isósceles')
   elif a==b!=c:
    print ('Você tem um triangulo isósceles')
   elif a==c!=b:
    print ('Você tem um triangulo isósceles')
   else:
    print ('Você tem um triangulo escaleno')
else:
    print ('não é um trigangulo')
    
    
   
    
