import random

number = 0
count = 0

print("Bienvenido al juego Adivina el Número")
print("Dame tu nombre")

name = input()
number = random.randint(1,20)

while count < 5:
  print("Adivina el número entre el 1 y el 20: ")
  guesNumber = input()
  guesNumber = int(guesNumber)
  count = count + 1
  if number == guesNumber:
    break
  if number < guesNumber:
    print("te pasaste ")
  if number > guesNumber:
    print("te falto ")


if number == guesNumber:
  print("Felicidades ganaste la partida")

if number != guesNumber:
  print("Has perdido la partida")