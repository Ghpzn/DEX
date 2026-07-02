print(10*'=')
print("Calculadora de Area 📐")
print(10*'=')

forma = int(input( '''Qual forma vc deseja para calcular a area?
  [1) Triangulo
   2) Retâmgulo
   3) Quadrado
   4) Circulo 
   5) Desistir] '''))
if forma ==1:
    height=int(input('  height '))
    base=int(input('  base '))
    tri=  (height* base)/2
    print(tri)
    
elif forma ==2:
    length=int(input(' Length '))
    width=int(input('  width '))
    re= length*width
    print(re)
elif forma ==3:
    side=int(input('Side '))
    qua= side**2
    print(qua)
    
elif forma ==4:
    radius=int(input('  Radius '))
    cir= 3.14*radius
    print(cir)
else:
   print('obrigado')



