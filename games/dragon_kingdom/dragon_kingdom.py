# Seccion de imports 

import random
import time

def showGameTitle():
  print("######################################")
  print("##       El Reino de Dragones       ##")
  print("######################################")

def showWelcomeMesage():
  print("Estas en un mundo lleno de dragones. Frente a ti hay dos cuevas.")
  print("En una de ellas se encuentra un terrible dragón hambriento en la otra un dragón amigable.")
  print("El dragón hamigable te compartirá de sus tesoros pero el hambriento te comerá")

def chooseCave():
  cave = ""
  while cave != "1" and cave != "2":
    print("¿A qué puerta quieres entrar? selecciona 1 o 2")
    cave = input()

  return int(cave)


def exploreCave(cave):
  print("............................")
  print("Te aproximas a la cueva...")
  time.sleep(2)
  
  print("Es una cueva obscura y tenebrosa")
  time.sleep(2)

  print("¡Un gran dragón se aproxima y abre sus fauces!")
  print("")
  time.sleep(2)

  safeCave = random.randint(1,2)

  if cave == safeCave:
    print("El dragón te regala sus tesoros mas preciados.")
    print(" 😎 ✌️ ¡Felicidades has ganado la partida!  😎 ✌️")
  else: 
    print("El dragón de traga de un mordisco ")
    print(" ☠️☠️☠️ ¡Has perdido la partida!  ☠️☠️☠️ ")

def goodBye():
  print("###########################################")
  print("##     Adios gracias por participar      ##")
  print("###########################################")


playAgain = "si"

showGameTitle()
showWelcomeMesage()

while playAgain == "si":
  cave = chooseCave()
  exploreCave(cave)

  print("")
  print("¿Quieres jugar de nuevo? selecciona si o no")
  playAgain = input()

goodBye()