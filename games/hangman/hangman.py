import random
import constants

MAX_FAIL = 6

def welcome():
      print("###########################################")
      print("##  Bienvenidos al juego del Ahorcado    ##")
      print("###########################################")

def good_bye():
      print("###########################################")
      print("##     Adios, gracias por participar     ##")
      print("###########################################")

def get_random_word():
      index = random.randint(0,len(constants.WORDS)-1)
      return constants.WORDS[index]

def print_board(index, word, correct_letters):
      if (index <= MAX_FAIL and index >= 0 ):
            print(constants.IMAGES[index])
      
      for letter in word:
            if(letter in  correct_letters):
                  print(letter, end=' ')
            else:
                  print('_', end=' ')
      print()

def choose_letter():
      print('Elije una letra')

      while True:
            letter = input()
            if len(letter) == 1 and letter.isalpha():
                  return letter.lower()
            else:
                  print("Elije solo una letra")

def game():
      secrete_word = get_random_word()
      fail_counter = 0
      correct_letters = []

      print("**************")
      print(secrete_word)

      while True:
            print_board(fail_counter, secrete_word, correct_letters)
            letter = choose_letter()

            
            if(letter in secrete_word):
                  print('correcto adivinaste una letra')
                  if not (letter in correct_letters):
                        correct_letters.append(letter)
                  if(set(secrete_word) == set(correct_letters)):
                        print("Ganaste")
                        break
            else:
                  fail_counter = fail_counter + 1
                  print('fallaste')
                  print_board(fail_counter, secrete_word, correct_letters)

                  if (fail_counter == MAX_FAIL): 
                        print('has perdido la partida')
                        break

playAgain = "si"
welcome()

while playAgain == 'si' or playAgain == 's' or playAgain == 'SI' or playAgain == 'S':
      game()
      print("")
      print("¿Quieres jugar de nuevo? selecciona si o no")
      playAgain = input()

good_bye()