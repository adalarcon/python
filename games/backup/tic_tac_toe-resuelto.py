respuesta="S"
jugada = 0
juego = False
X=0
Y=0
resultado = ""
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
# Dibuja Tablero
def dibuja_matriz():
    print(" %c | %c | %c " % (matriz[0][0],matriz[0][1],matriz[0][2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (matriz[1][0],matriz[1][1],matriz[1][2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (matriz[2][0],matriz[2][1],matriz[2][2]))    
# Valida el estado de la jugada en el tablero
def valida(trn):
    global resultado
    # Horizontal y Vertical
    for i in range(0,3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != " " or matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            resultado="gana "+trn
            return True
    # Diagonal
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " " or matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        resultado="gana "+trn
        return True
    # Todo lleno
    if " " not in matriz[0] and " " not in matriz[1] and " " not in matriz[2]:
        resultado="Empate"
        return True
    # Por Default
    return False
 
def nuevo_juego():
    for i in range(0,3):
        matriz[i][0] = " " 
        matriz[i][1] = " " 
        matriz[i][2] = " "
 
print("---------------------------------------")
print("Tateti                                 ")
print("---------------------------------------")
while respuesta.upper()!="N":
    try:
        Turno="X"
        nuevo_juego()
        juego=False
        # Lazo del juego si gano o tablas
        if respuesta.upper()=="S":
            while juego==False:
                dibuja_matriz()
                print("Juega ",Turno," ",end="")
                # exception del valor cuando es ENTER ''
                try:
                    jugada=int(input("donde juega?(1-9):"))
                except ValueError:
                    print("No es un numero")
                except KeyboardInterrupt:
                    print("No es un numero")
                else:
                    if jugada <=9 and jugada >=1:
                        jugada=jugada-1
                        Y = jugada/3
                        X = jugada%3
                    X = int(X)
                    Y = int(Y)
                    if matriz[Y][X] == " ":
                        matriz[Y][X] = Turno
                        juego=valida(Turno)
                        if Turno == "X":
                            Turno = "O"
                        else:
                            Turno = "X"
                    else:
                        print("Ocupada, intente otra jugada!")
                    # Cambio de turno
        if resultado != "" :
            print("***************************")
            print("Fin de la Jugada!!!!!!!!!!")
            print("***************************")
            print(resultado)
            print("***************************")
            dibuja_matriz()
        respuesta=input("Jugar Otra vez? (S/N)")
        resultado=""
    except KeyboardInterrupt:
        print ("Selecione una opcion correcta!!")
        respuesta=""
        resultado=""
print("Fin. Gracias por Jugar.")