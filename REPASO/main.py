
#1.crear un programa que me pida la edad de una persona si
#la edad es mayor o igual a 18 que me muestre un mensaje 'eres 
#mayor de edad' caso contrario que me muestre un mensaje 'eres menor de edad


edad = int(input("17: "))

if edad >= 18:
   print("Eres mayor de edad.")
else:
   print("Eres menor de edad.")

#2.Una tienda comercial desea hacer un descueto del 20%, crear 
#un programa que me determine si el cliente se hace acreedor del
#descueto teniendo encuenta los siguiente, si el cliente realiza 
#una compra de igual o mayor a 1000 soles mostrar un mensaje que
#diga 'ganaste el descuento del 20% ahora pagaras <mostrar el 
#total de la compra menos el descuento en caso la compra no
#supere los 1000 soles entonces mostrar un mensaje que diga 'no
#aplicas al descuento <mostrar el monto de la compra>'


monto_compra = float(input("Ingrese el monto de la compra en soles: "))

if monto_compra >= 1000:
    descuento = monto_compra * 0.2
    total_con_descuento = monto_compra - descuento
    print("¡Ganaste el descuento del 20%! Ahora pagarás:", total_con_descuento, "soles.")
else:
    print("No aplicas al descuento. El monto de tu compra es:", monto_compra, "soles.")
    
    
    #3 crear un programa que me pida 5 veces un nombre y por cada vez que lo 
    # pida muestre la cantidad de veces que ingreso el nombre
   
    
    for n in range(1,6):
       nombre=input("ingrese su nombre:")
       print(f"ingresaste {n} veces el nombre")
    
    #4 crear un programa que pida un numero 
    # y lo evalue con el numero premiado si el
    # numero ingresado es el premiado el programa finalizara si el numero ingresado
    # es incorrecto el programa seguira pidiendo el numero premiado

numero_premiado = 1234
numero_ingresado = int(input("Ingrese un número: "))

while numero_ingresado != numero_premiado:
    print("Número incorrecto. Inténtelo nuevamente.")
    numero_ingresado = int(input("Ingrese otro número: "))

print("¡Felicidades! Ha ingresado el número premiado. El programa ha finalizado.")