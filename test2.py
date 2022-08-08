import random


def random_door():
  doors = ["cabra", "cabra", "cabra"]
  doors[random.randint(0, 2)] = "coche"
  return doors


# Monty Hall open a door
def open_door(door_selected, doors):
  open = door_selected
  if (doors[door_selected] == "coche"):
    open = random.randint(0, 2)
    while (open == door_selected):
      open = random.randint(0, 2)
    doors[open] = "open"
  else:
    index = doors.index("coche")
    while ((open == door_selected) or (open == index)):
      open = random.randint(0, 2)
    doors[open] = "open"

  return doors


def main():

  attemps = 1000000
  win = 0
  lose = 0

  for i in range(attemps):

    doors = random_door()  # Generate the doors 
 
    player_selection = random.randint(0, 2)  # Player selects the door

    # Monty Hall opens a door with a goat
    doors = open_door(player_selection, doors)

    # Player changes of door
    if (player_selection == doors.index("coche")):
      player_selection = doors.index("cabra")

    elif (player_selection == doors.index("cabra")):
      player_selection = doors.index("coche")

    # Count of victories and defeats
    if doors[player_selection] == "coche":
      win += 1
    else:
      lose += 1
    

  print(f"{attemps} Intentos")
  print(f"Numero de victorias: {win} ")
  print(f"Numero de derrotas: {lose} ")

  print("Porcentajes de victorias: {:.2f}%".format(((win/attemps)*100)))

if __name__ == "__main__":
  main()