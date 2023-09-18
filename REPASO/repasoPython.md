# Repaso Python
# 1. Tipos de Datos
``"a"``  ***string cadena de texto***

``"hola"`` ***esto tambien es un string***

``"hola soy un string y te saludo"``  ***cadena larga***

### OBSERVACION :todo lo que ete entre comillas es un string
``"100"``

``"False"``

``"hola"``

### un string puede estar entre comillas simples o dobles

``100`` ***este es un tipo de dato numerico entero***

``2.1`` ***es un tipo de dato numerico de tipo flotante float.***

``False`` ***este es un tipo de dato booleano falso***

``True`` ***tipo de dato booleano verdadero***
# 2. Variables
 - ***Es donde almacenamos nuestro tipo de dato 
 esos datos pueden mutar cambiar o modificarse
como creamos una variable para almacenar nuestro datos. darle un nombre significativo o relacionado al dato que estamos almacenando***

-  ***Indiacarle a que dato esta relacionado -> asignacion =***

 - ***indicar el tipo de dato que se va almacenar -> darle el dato a guardar***

 ### primero el dato voy a pedir la edad de nadine
 ``edad_nadine=18``
 ### el nombre de un alumno
 ``nombre_alumno="edwin"``

# 3. Operadores

1. **operadores aritmeticos**
- *suma+*
- *resta-*
- *multiplicacion**
- *divicion /*


*suma* = ``45+12``

*resta* =``45-12``

*multi*=``2*5``

*divi*=``4/2``

*operacion*=``(45+12+23)/4``

**op**=``15+12+14+13/4``
### operadores de uso especial
#### - suma=45+42   *operador suma resultado 87*

#### - suma="45"+12 *operador concatenacion resultado 4512*

#### - saludo="hola"+"mundo" *concatenacion holamundo*

#### - saludo2="hola"+" "+"mundo"  *concatenar hola mundo*

#### - saludos="hola"*2 *holahola*


# 4. Datos Estructurados
### listas
#### puede alamacenar distintos tipos de datos en una sola lista separados por comas
``lista=["nombre",10,False]``

``lista-amigos=["jory","edwin","adan","chinita"]``
### objetos



- tambien al igual que las listas alamacenan distintos tipos de datos con un orden.
- para almacenar datos en un objeto necesitamos especificar un indice y un valor clave->valor
```python
alumno={
     "nombre":"jory",
    "edad":52,
    "sexo":"todos los dias"

}
```

### combinar ambas estructuras de datos
```python
``alumno={

    "nombre":"jory",
    "edad":30,
    "amigos":["anthony","edwin","china"],
    "direccion":{
        "departamento","ayacucho",
        "provincia","lucanas",
        "distrito","puquio",
        "jiron","san piter",
        "numero",152
    }

}
```
``alumnos=[{},{},{}]

# 5. Controles de flujo
## - Decisiones
***solo se ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condiciciòn sea falsa se ejecuta otro codigo***
## Sintaxis
***primero especificar el codigo que se ejecutara si cumple una condicion***

``if <condicion>:``

**el codigo que deseamos ejecutar si la condicion es verdadera**
print("ejecuta esto")
**aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if**
``print("esto siempre ejecutara")``

### si queremos que se ejecute un codigo en caso sea falso 
```python
if <condicion falsa>:
  print("solo imprime si es verdad")
else:
  print("solo imprime  si es falso")

```
**ejemplito**
```python
if 15>18:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

condicion=True
if condicion:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

    
        
```
## - Ciclos

***existen dos tipos:***
## - cuando sabes la cantidad de veces que vamos a repetir 

- *para este caso existe el for*
- *sintaxis despues de la palabra reservada for deberemos crear una variable que almacene el numero que iremos iterando*
- *luego tendremosque indicar el rango interar a los elementos a itear*
```python 
vocales=("a","e","i","o","u")
for i in vocales:
    print(i)
```
# FUNCIONES 
 ## existen dos tipos 

 ### 1. propias de lenguaje
 ## que ya vienen creadas e insertadas en python y estan listas para ser usadas
 ## estructura de uso de una funcion
 ## tiene el nombre seguido de parentesis podremos pasarle datos que necesita la funcion para ejecutarse 

 ## esta es una funcion que nos sirve para mostrar por consola datos 
 print('hola') 

 ## esta funcion nos saber la longitud de una lista o un string
***len nos devuelve un numero***
```python
print(len([1, 5, 6, 7, 8]))
```

# es una funcion que se detiene a esperar que el usuario introdusca informacion 
# entre parentesis podremos escribr un mensaje que indique que accion realizara el usuario 
```python
input('ingresa ingresa')
```














