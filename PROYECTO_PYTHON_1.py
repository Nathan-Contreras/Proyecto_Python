import random
import time

intentos = 0

while True:
  print("Que te gustaria jugar hoy?\n1. Adivina el número\n2. Piedra, papel o tijera\n3. Salir")
  opcion = int(input("==> "))

##############        ADIVINA EL NUMERO         ##############
  if opcion == 1:
    print("Bienvenido al juego de adivinar el número")
    time.sleep(2)
    print("Estoy pensando en un número entre 1 y 100...")
    ad = random.randint(1, 100)
    adivina = int(input("Adivina el número: "))
    intentos += 1
    if adivina == ad:
      print(f"\n\nFelicidades!!!!! Adivinaste el número en el primer intento!!!!!\n\n")
      intentos = 0
    else:
      while adivina != ad and intentos < 5:
        if adivina < ad:
          print("El número es mayor")
          adivina = int(input("Adivina el número: "))
          intentos += 1
        elif adivina > ad:
          print("El número es menor")
          adivina = int(input("Adivina el número: "))
          intentos += 1
        if adivina == ad:
          print(f"\n\nFelicidades! Adivinaste el número en {intentos} intentos\n\n")
          intentos = 0
          break
    if intentos == 5:
      print("\n\nLo siento, has llegado al límite de intentos\n\n") 

##############        PIEDRA, PAPEL O TIJERA        ##############
  elif opcion == 2:
    print("Bienvenido al juego de piedra, papel o tijera")
    time.sleep(2)
    ptj_jugador = 0
    ptj_computadora = 0
    print("Vamos a jugar")

    while True:
      print("1. Piedra\n2. Papel\n3. Tijera\n4. Salir")
      jugador = int(input("Elige una opción: "))

      if jugador == 1:
        seleccion = "Piedra"

      elif jugador == 2:
        seleccion = "Papel"

      elif jugador == 3:
        seleccion = "Tijera"

      elif jugador == 4:
        print("PUNTAJES:\nJugador: ", ptj_jugador, "\nComputadora: ", ptj_computadora)
        if ptj_jugador > ptj_computadora:
          print("\n\nFelicidades! Has ganado\n\n")
        elif ptj_jugador < ptj_computadora:
          print("\n\nLo siento, has perdido\n\n")
        else:
          print("\n\nHa sido un empate!\n\n")

        time.sleep(2)
        print('\n')
        break
      else:
        print("Opción no válida")
        time.sleep(2)
        print("\n")
        continue
      print(f"Tu seleccion: {seleccion}")

      computadora = random.randint(1, 3)
      if computadora == 1:
        seleccion_computadora = "Piedra"
      elif computadora == 2:
        seleccion_computadora = "Papel"
      else:
        seleccion_computadora = "Tijera"

      if jugador == computadora:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Empate")

      elif jugador == 1 and computadora == 2:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Computadora gana")
        ptj_computadora += 1

      elif jugador == 1 and computadora == 3:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Tu ganas")
        ptj_jugador += 1

      elif jugador == 2 and computadora == 1:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Tu ganas")
        ptj_jugador += 1

      elif jugador == 2 and computadora == 3:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Computadora gana")
        ptj_computadora += 1

      elif jugador == 3 and computadora == 1:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Computadora gana")
        ptj_computadora += 1

      elif jugador == 3 and computadora == 2:
        print(f"Computadora seleccionó: {seleccion_computadora}")
        print("Tu ganas")
        ptj_jugador += 1
      time.sleep(2)

      
  elif opcion == 3:
    print("Gracias por jugar")
    print("Saliendo...")
    time.sleep(2)
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    break

  else:
    print("Opción no válida")
    print("Por favor, elige una opción válida")
    time.sleep(2)
    print("\n")