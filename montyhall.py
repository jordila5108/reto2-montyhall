# Monty Hall problema
import random

# Array con premios de las puertas
def random_door():
  doors = ["cabra", "cabra", "cabra"]
  doors[random.randint(0, 2)] = "premio"
  return doors


# Monty Hall abre una puerta
def open_door(player_sel, doors):
  open = player_sel
  if (doors[player_sel] == "premio"):
    open = random.randint(0, 2)
    while (open == player_sel):
      open = random.randint(0, 2)
    doors[open] = "open"
  else:
    index = doors.index("premio")
    while ((open == player_sel) or (open == index)):
      open = random.randint(0, 2)
    doors[open] = "open"

  return doors


def main():

  intentos = 1000000
  victorias = 0
  derrotas  = 0

  for i in range(intentos):
    # Generar las puertas
    doors = random_door()

    # El jugador selecciona la puerta
    player_selection = random.randint(0, 2)

    # Monty Hall abre una puerta con una cabra
    doors = open_door(player_selection, doors)

    # Cambios de jugador de puerta
    if (player_selection == doors.index("premio")):
      player_selection = doors.index("cabra")

    elif (player_selection == doors.index("cabra")):
      player_selection = doors.index("premio")

    # Cuenta de victorias y derrotas
    if doors[player_selection] == "premio":
      victorias = victorias + 1
    else:
      derrotas = derrotas + 1

  print(f"{intentos} intentos")
  print(f"ganaste {victorias} veces.")
  print(f"perdiste {derrotas} veces.")

  print("porcentaje de ganancia: {:.2f}%".format(((victorias/intentos)*100)))


if __name__ == "__main__":
  main()