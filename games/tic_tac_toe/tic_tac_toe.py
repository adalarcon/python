import random

X_SIMBOL = "👿"
O_SIMBOL = '🎃'

def welcome():
      print("############################################")
      print("##  Bienvenidos al juego del TIC TAC TOE  ##")
      print("############################################")

def good_bye():
      print("###########################################")
      print("##     Adios, gracias por participar     ##")
      print("###########################################")

def print_board(board):
  print()
  for i in range(len(board)):
    print(" %c | %c | %c " % (board[i][0], board[i][1], board[i][2] ))
    if(i != len(board) - 1):
      print("-----------")
  print()

def get_turn():
  return random.choice([X_SIMBOL, O_SIMBOL])

def change_board(board, turn, n):
  index = n-1
  x = index // 3
  y = index % 3
  if board[x][y] != X_SIMBOL and board[x][y] != O_SIMBOL:
    board[x][y] = turn
    return True
  return False

def make_move(board, turn):
  while True:
    print("Es turno de %c, seleccione un numero: (1 al 9)" %(turn))
    n = input()
    if (n.isdigit()):
      n = int(n)
      if(n >= 1 and n <= 9):
        if change_board(board,turn, n):
          return
        else:
          print("La casilla ya esta ocupada, seleccione otra")
        

def change_turn(turn):
  if(turn == X_SIMBOL): 
    return O_SIMBOL
  else:
    return X_SIMBOL

def check_if_winner(board, turn):

  # Revisar ganador en reglones y columnas
  for i in range(len(board)):
    if board[i][0] == turn and board[i][1] == turn and board[i][2] == turn:
      print("Gano por renglon %d el turno %c" %(i, turn))
      return True

    if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:
      print("Gano por columna %d el turno %c " %(i, turn))
      return True

  # Revisar ganador por diagonal
  if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
      print("Gano por diagonal 1 el turno %c " %(turn))
      return True

  # Revisar ganador por diagonal
  if board[2][0] == turn and board[1][1] == turn and board[0][2] == turn:
      print("Gano por diagonal 2 el turno %c"  %(turn))
      return True

  return False

def game():
  board = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '], 
    [' ', ' ', ' ']
  ]
  move_counter = 0
  turn = get_turn()
  print_board(board)
  finished = False
  while not finished:
    make_move(board, turn)
    move_counter = move_counter + 1
    print_board(board)

    if move_counter >= 5:
      if check_if_winner(board, turn):
        print("¡¡¡ Felicidades el turno ganador es %c !!!" %(turn))
        finished = True

    if move_counter >= 9:
      finished = True

    turn = change_turn(turn)
    
playAgain = "si"
welcome()

while playAgain == 'si' or playAgain == 's' or playAgain == 'SI' or playAgain == 'S':
      game()
      print("")
      print("¿Quieres jugar de nuevo? selecciona si o no")
      playAgain = input()

good_bye()