edad = 15


if edad >= 18:
   print("Eres mayor de edad.")

else:
   print("eres menor de edad.")

# IF-ELIF-ELSE

calificacion = 85


if calificacion >= 90:
   print("Excelente")

elif calificacion >= 80:
   print("Muy bueno")

elif calificacion >= 70:
   print("Bueno")

else:
   print("Necesita mejorar")


time_hour = 8
mood = "sleepy"
if time_hour >= 0 and time_hour <= 24:
   print('Suggesting a drink option...')
if mood == 'sleepy' and time_hour < 10:
      print('coffee')
elif mood == 'thirsty' or time_hour < 2:
      print('lemonade')
else:
      print('water')
      
      
if time_hour < 10: print('coffee') 
else: print('water')

   # CICLO FOR

for i in range(5):
   print(i)     

# imprime ciclo los elementos de una tupla  
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# CICLO WHILE
contador = 0

while contador < 5:

    print(contador)
    contador += 1


# control de ciclo con BREAK

contador = 0

while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

# instruccion continue  
print("*" * 20)
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

print("*" * 20)
print("inicio del ciclo con instruccion pass")
"""La instrucción pass es una operación nula que no hace nada. 
    Se utiliza como marcador de posición cuando se requiere una 
    instrucción sintácticamente, pero no se desea realizar ninguna acción.

    Esto puede ser útil cuando se está desarrollando un 
    programa y se desea reservar un bloque de código para 
    implementarlo más adelante.
"""
for i in range(5):
    pass