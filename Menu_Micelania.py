def MostrarMenu ():
    print('Bienvenido a la micelania de trabajos porfavor selecione alguna opcion de nuestro menu')
    print('===Menu===')
    print('1. area de triangulo')
    print('2. suma de dos numeros')
    print('3. potencia de un numero')
    print('4. la suma de 1234 y 532')
    print('5. resta entre 1234 y 532')
    print('6. multiplicacion de 1234 y 532')
    print('7. Division de 1234 y 532')
    print('8. Modulo entre 1234 y 532')
    print('9. Convercion de moneda')
    print('10. Area de rectangulo')
    print('11. Area y Perimetro de un cuadrado')
    print('12. Area y Volumen de cilindro')
    print('13. Area y longitud de una circunferencia')
    print('14. Promedio de 3 numeros')
    print('15. numero negativo y positivo')
    print('16. menor y mayor')
    print('17. menor y mayor de 3 numeros')
    print('18. calcular el sueldo de los empleados')
    print('19. dos numeros  si los voy a sumar')
    print('20. divicion entre 0')
    print('21. dia de la semana')
    print('22. logitudes de triangulo')
    print('23. sumar pero si es negativo multiplicar')
    print('24. signo zodiacal')
    print('25. cuadrado o rectangulo')
    print('26. descuentos en tienda')
    print('27. saber si el año es bisiesto')
    print('28. mutiplos de 3')
    print('29. numeros impares')
    print('30. numeros pares')
    print('31. numeros del 1 al 3')
    print('32. numeros del 10 al 1')
    print('33. cuadrados del 1 al 30')
    print('34. suma de los cuadrados')
    print('35. hallar el factorial')
    print('36. hallar el factorial')
    print('37. de fahrenheit a celsius')
    print('38. numero primos')
    print('39. tablas de multiplicar')
    print('40. promedio de numeros positivos')
    print('41. asendencia de dos numeros')
    print('42. domino')
    print('43. SALIR')
while True:
     MostrarMenu()
     option=input('selecione una opcion: ')
     if option=='1':
#area de triangulo
          def AreaTriangle (base, height):
             area=(base*height)/2
             return area
          base=int(input('ingrese la base del triangulo: '))
          height=int(input('ingrese la altura del triangulo: '))
          result=AreaTriangle (base, height)
          print('el area del triangulo es: ', result)
     elif option=='2':
#suma de dos numeros
         def Sumnumeros (num1, num2):
             sum=num1+num2
             return sum
         num1=int(input('ingrese el primer numero: '))
         num2=int(input('ingrese el segundo numero: '))
         result2=Sumnumeros (num1, num2)
         print('la suma de los dos numero es: ', result2)
     elif option=='3':
#potencia de un numero
         def Powernumero (numero):
             power= numero**2
             return power
         numero=int(input('ingrese el numero que desea ver: '))
         pow=Powernumero(numero)
         print('el cuadrado es: ', pow)
     elif option=='4':
#la suma de 1234 y 532
          def SumTwo (numb1,numb2 ):
             sum2=numb1+numb2
             return sum2
          numb1=1234
          numb2=532
          su=SumTwo (numb1,numb2)
          print('la suma de los dos numero es: ', su)
     elif option=='5':
#resta entre 1234 y 532
         def Subtract (min,subt):
             sub=min-subt
             return sub
         min=1234
         subt=532
         res=Subtract (min, subt)
         print('la resta de los dos numeros es: ', res)
     elif option=='6':
#multiplicacion  entre 1234 y 532
         def Multiplication (mul1,mul2):
             mult=mul1*mul2
             return mult
         mul1=1234
         mul2=532
         mul= Multiplication(mul1, mul2)
         print('el resultado de la multiplicacion es: ', mul)
     elif option=='7':
#divesion entre 1234 y 532
         def Divesion (divid,dives):
             divi=divid/dives
             return divi
         divid=1234
         dives=532
         divesion= Divesion(divid,dives)
         print=('el resultado de la divesion es: ', divesion)
     elif option=='8':
#modulo entre 1234 y 532
          def Module(numero1,numero2):
             mod=numero1%numero2
             return mod
          numero1=1234
          numero2=532
          module=Module(numero1, numero2)
          print=('el residuo de la divesion es: ', module)
     elif option=='9':
#conversion de moneda
          moneda=int(input("escriba 1 para convertir euros a dolares y 2 para convertir dolares a euros: "))
          if moneda == 1: 
              def ConversionEuro (euro):  
                 convercion=euro*1.09
                 return convercion
              euro=float(input('ingrese la cantgidad de euros que desea convertir: '))
              money=ConversionEuro (euro)
              print(euro ,"euros son: $", money ,"dolares")
          elif moneda == 2:
               def ConversionDolar (dolar):
                 convercion2=dolar*0.91
                 return convercion2
               dolar=float(input('ingrese la cantidad de dolares que desea convertir: '))
               money2=ConversionDolar (dolar)
               print(dolar ,"dolares son: €", money2 ,"euros")
     elif option=='10':
         #area rectangulo
         def AreaRectangle (base2, height2):
             area2=base2*height2
             return area2
         base2=float(input('ingrese la base del rectangulo: '))
         height2=float(input('ingrese la altura del rectangulo: '))
         Area=AreaRectangle(base2, height2)
         print('el area del rectangulo es: ', Area)
     elif option=='11':
         #area y perimetro cuadrado
         def AreaPeresquare (side):
             area3=side**2
             perimeter=side*4
             return area3,perimeter
         side=float(input('ingrese la medida de  algun lado: '))
         Area2= AreaPeresquare (side)
         print('el area y perimetro del cuadrado es: ', Area2)
     elif option=='12':
         #area y volumen cilindro
         def AreaVolCylinder (radius, height3):
             area4=(2*3.14)*radius*height3+(2*3.14)*(radius**2)
             volume=3.14*(radius**2)*height3
             return area4,volume
         radius=float(input('ingrse el radio del cilindro: '))
         height3=float(input('ingrese la altura del cilindro: '))
         Volume= AreaVolCylinder (radius,height3)
         print('el area y volumen del cilindro es: ', Volume)
     elif option=='13':
         #area y longitud circunferencia
         def AreaLegCircumference (radius2):
             length=(2*3.14)*radius2
             area5=3.14*(radius2**2)
             return length, area5
         radius2=float(input('ingrese el radio de la circunferencia: '))
         length2=AreaLegCircumference(radius2)
         print('la longitud y area de la circunferencia es: ', length2)
     elif option=='14':
         #promedio de 3 numeros
         def AverageTree (numero1, numero2, numero3):
             average= (numero1+numero2+numero3)/3
             return average
         numero1=float(input(' ingrese el primer numero: '))
         numero2=float(input('ingrese el segundo numero: '))
         numero3=float(input('ingrese el tercer numero: '))
         Averrage=AverageTree (numero1, numero2, numero3)
         print('el promedio de los tres numeros es: ', Averrage)
     elif option=='15':

    # numero negativo y positivo
         numero = int(input('ingrse el numero: '))
         if numero > 0:
             print('el numero' + str(numero) + 'es positivo')
         elif numero < 0:
             print('el numero ' + str(numero) + ' es negativo')
         else:
             print('el numero ' + str(numero) + ' es neutral')
     elif option=='16':
    # menor y mayor
         num1 = int(input('ingrese el primer numero: '))
         num2 = int(input('ingrese el segundo numero: '))
         if num1 > num2:
             print(str(num1) + ' es el mayor y ' + str(num2) + ' es el menor')
         elif num1 < num2:
             print(str(num2) + ' es el mayor y ' + str(num1) + ' es el menor')
         else:
             print('los numero son iguales')

     elif option=='17':
    # menor y mayor de 3 numeros
          Num1 = int(input('ingrese el primer numero: '))
          Num2 = int(input('ingrese el segundo numero: '))
          Num3 = int(input('ingrese el tercer numero: '))
          if Num1 > Num2 > Num3:
             print(str(Num1) + ' es el mayor, ' + str(Num2) + ' es el intermedio y ' + str(Num3) + ' es el menor')
          elif Num1 > Num3 > Num2:
             print(str(Num1) + ' es el mayor, ' + str(Num3) + ' es el intermedio y ' + str(Num2) + ' es el menor')
          elif Num2 > Num1 > Num3:
             print(str(Num2) + ' es el mayor, ' + str(Num1) + ' es el intermedio y ' + str(Num3) + ' es el menor')
          elif Num2 > Num3 > Num1:
             print(str(Num2) + ' es el mayor, ' + str(Num3) + ' es el intermedio y ' + str(Num1) + ' es el menor')
          elif Num3 > Num2 > Num1:
             print(str(Num3) + ' es el mayor, ' + str(Num2) + ' es el intermedio y ' + str(Num1) + ' es el menor')
          elif Num3 > Num1 > Num2:
             print(str(Num3) + ' es el mayor, ' + str(Num1) + ' es el intermedio y ' + str(Num2) + ' es el menor')
          else:
             print('los numeros son iguales')

     elif option=='18':
    # calcular el sueldo de los empleados
          name = input('bienvenido, ingrese el nombre del empleado: ')
          hours_1 = int(input('ingrese las horas trabajadas: '))
          hours_2 = int(input('ingrese las horas extras: '))
          pay = (hours_1 * 4) + (hours_2 * 8)
          print('The pay of ' + str(name) + ' es $' + str(pay))

     elif option=='19':
    # dos numeros  si los voy a sumar
         d1 = int(input('ingrese el primero numero: '))
         d2 = int(input('ingrese el segundo numero: '))
         if d1 < d2:
             result = d1 + d2
             print('el resultado es: ' + str(result))
         else:
             result2 = d1 - d2
             print('el resultado es: ' + str(result2))

     elif option=='20':
    # divicion entre 0
         c1 = int(input('ingrese el dividendo: '))
         c2 = int(input('ingrese el divisor: '))
         if c2 == 0:
             print('esta divicion no es posible')
         else:
             res = c1 // c2
             print('el resultado es: ' + str(res))

     elif option=='21':
    # dia de la semana
         day_week = int(input('Enter a numero (1-7): '))
         if day_week == 1:
             print('el numero 1 es LUNES')
         elif day_week == 2:
             print('el numero 2 es MARTES')
         elif day_week == 3:
              print('el numero 3 es MIERCOLES')
         elif day_week == 4:
             print('el numero 4 es JUEVES')
         elif day_week == 5:
             print('el numero 4 es VIERNES')
         elif day_week == 6:
             print('el numero 4 es SABADO')
         elif day_week == 7:
             print('el numero 4 es DOMINGO')
         else:
             print('el numero no es valido')

     elif option=='22':
    # logitudes de triangulo
         side_1 = int(input('ingresa el primer lado del triangulo: '))
         side_2 = int(input('ingresa el segundo lado del triangulo: '))
         sied_3 = int(input('ingresa el tercer lado del triangulo: '))
         if side_1 == side_2 == sied_3:
             print('el triangulo es equilatero')
         elif side_1 == side_2 != sied_3:
             print('el triangulo es esosceles')
         elif side_1 != side_2 != sied_3:
             print('el triangulo es escaleno: ')
         else:
             print('thes triangle es esosceles')

     elif option=='23':
    # sumar per si es negativo multiplicar
         num_1 = int(input('ingresa el primer numero: '))
         num_2 = int(input('ingresa el segundo numero: '))
         if num_1 < 0 or num_2 < 0:
             res_1 = num_1 + num_2
             print('el resultado es: ' + str(res_1))
         else:
             res_2 = num_1 * num_2
             print('el resultado es: ' + str(res_2))

     elif option=='24':
    # signo zodiacal
         day = int(input('ingresa tu dia de nacimiento: '))
         mount = int(input('ingresa tu mes de nacimiento: '))
         if (mount==3 and day>=21) or (mount==4 and day<=20):
             print('Aries')
         elif (mount==4 and day>=21) or (mount==5 and day<=20):
             print('Tauro')
         elif (mount == 5 and day >= 21) or (mount == 6 and day <= 20):
             print('Gemines')
         elif (mount==6 and day>=21) or (mount==7 and day<=22):
             print('Cancer')
         elif (mount==7 and day>=23) or (mount==8 and day<=23):
             print('Leo')
         elif (mount==8 and day>=24) or (mount==9 and day<=22):
             print('Virgo')
         elif (mount==9 and day>=21) or (mount==10 and day<=20):
             print('Libra')
         elif (mount==10 and day>=24) or (mount==11 and day<=22):
             print('Escorpio')
         elif (mount==11 and day>=21) or (mount==12 and day<=22):
             print('Sagitario')
         elif (mount==12 and day>=22) or (mount==1 and day<=20):
             print('Capricornio')
         elif (mount==1 and day>=21) or (mount==2 and day<=19):
             print('Acuario')
         elif (mount==2 and day>=20) or (mount==3 and day<=20):
             print('Pesces')
         else:
             print('el numero no es valido ')

     elif option=='25':
    #cuadrado o rectangulo
         base = int(input('ingrese el base of the quadrilateral: '))
         height = int(input('ingrese el height of the quadrilateral: '))
         area= base*height
         perimeter = base + height + base +height
         if base != height:
             print('es un rectangulo')
         else:
             print('es un cuadrado')
         print('el area es: '+ str(area))
         print('el perimetro es: '+ str(perimeter))

     elif option=='26':
    #descuentos en tienda
         purchase=float(input('ingrese el precion inicial: '))
         if purchase<100:
             price_off=purchase*0.05
             price_total=purchase-price_off
             print('el precio total es: $' + str(price_total))
         elif purchase>200:
             price_off = purchase * 0.15
             price_total = purchase - price_off
             print('el precio total es: $' + str(price_total))
         else:
             price_off = purchase * 0.10
             price_total = purchase - price_off
             print('el precio total es: $' + str(price_total))
     elif option=='27':
    #saber si el año es besiesto
         year=int(input('ingrese el año: '))
         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
             print('es año besiesto')
         else:
             print('no es año besiesto')
     elif option=='28':
         #mutiplos de 3
         for i in range (101):
             if i %3==0:
                 print (i)
     elif option=='29':
         #numeros impares
         for num in range (101):
             if num %2 !=0:
                 print(num)
     elif option=='30':
         #numeros pares
         for Par in range (101):
             if Par %2==0:
                 print(Par)
     elif option=='31':
         #numeros del 1 al 3
         for up in range(1,4):
             print (up)
     elif option=='32':
         #numeros del 10 al 1
         for down in range(10, 0, -1):
             print(down)
     elif option=='33':
         #cuadrados del 1 al 30
         for power2 in range (1, 31):
             square=power2**2
             print(square)
     elif option=='34':
         #suma de los cuadrados
         SUM=0
         for square2 in range(101):
             SUM += square2**2
             print(SUM)
     elif option=='35': 
         #hallar el factorial
         NUM=int(input('ingrese un numero: '))
         sum=0
         for m in range(NUM(NUM+101)):
             sum += m
             print(sum)
     elif option=='36':
         #hallar el factorial
         number=int(input('ingrese un numero: '))
         factorial=1
         if number < 0:
             print('el factorial no esta disponible en numero negativos')
         elif number ==0:
             print('el factorial de 0 es 1')
         else: 
             for f in range (1, number + 1):
                 factorial *= 1
                 print('el factorial de', number , 'es: ', factorial)
     elif option=='37':
         #de fahrenheit a celsius
         def ConverFahToCel (fahrenheit):
             celsius=(fahrenheit-32)*5/9
             return celsius
         while True:
             TemFahrenheit=float(input('ingrese la temperatura en grados: '))
             if TemFahrenheit==999:
                 print('finalizar convercion')
                 break
             TemCelsius = ConverFahToCel (TemFahrenheit)
             print('la temperatura en grados Celsius es: ', TemCelsius)
     elif option=='38':
         #numero primos
         def NumberPrime (num):
             if num <2:
                 return False
             for prime in range(2, int(num**0.5)+1):
                 if num %prime == 0:
                     return False
                 return True
             limit= int(input('ingrese el limite de la lista: '))
             print('estos son los numeros primos hasta', limit,':')
             for n in range(2, limit+1):
                 if NumberPrime(n):
                     print(n)
     elif option=='39':
         #tablas de multiplicar
         number2=int(input('ingrese el el numero que desea ver la tabla de multiplicaciones: '))
         for num in range (1, 13):
             result3=number2*num
             print(number2 , 'x', num, '=', result3)
     elif option=='40':
         #promedio de numeros positivos
         sum2=0
         cont=0
         while True:
             number3=int(input('ingrese un numero positivo: '))
             if number3 <0:
                 break
             sum2 += cont
             cont+=1
             if cont>0:
                 average2=sum2/cont
                 print('el promedio es:', average2)
     elif option=='41':
         #asendencia de dos numeros
         num3=int(input('ingrese el numero menor: '))
         num4=int(input('ingrese el numero mayor: '))
         for d in range(num3+1, num4):
             print(d)
     elif option=='42':
         #domino
         for c1 in range(7):
             for c2 in range(c1, 7):
                 print('ficha ', c1, '-', c2)
     elif option=='43':
         print('Adios')
         break
     else:
         print('este numero no se encuetra disponible')


                  