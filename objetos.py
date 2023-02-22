from personaje import *

#1. Solicitamos los datos para los objetos

#Heroe
print("")
print("### Solicitud Datos Heroe ###")
espescieH = input("Escribe la especie del Heroe: ")
nombreH = input("Escribe el nombre del Heroe: ")
alturaH = float(input("Escribe la altura del Heroe: "))
recargarH = int(input("Ingresa las balas para el Heroe: "))

#Villano
print("")
print("### Solicitud Datos Villano ###")
espescieV = input("Escribe la especie del Villano: ")
nombreV = input("Escribe el nombre del Villano: ")
alturaV = float(input("Escribe la altura del Villano: "))
recargarV = int(input("Ingresa las balas para el Villano: "))

#1. Creamos una instancia de la clase Personaje
Heroe = Personaje(espescieH, nombreH, alturaH)
Villano = Personaje(espescieV, nombreV, alturaV)

#2. Usamos los atributos 
print("El personaje se llama: " + Heroe.nombre)
print("Pertenece a la especie: " + Heroe.especie)
print("y una altura de: " + str(Heroe.altura))
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargarH)

print("El personaje se llama: " + Villano.nombre)
print("Pertenece a la especie: " + Villano.especie)
print("y una altura de: " + str(Villano.altura))
Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargarV)



