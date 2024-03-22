class Character:
  def __init__(self, Name, XPosition, YPosition):
    self.Name = Name # of data type STRING
    self.XPosition = XPosition # of data type INTEGER
    self.YPosition = YPosition # of data type INTEGER

  def GetXPosition(self):
    return self.XPosition

  def GetYPosition(self):
    return self.YPosition

  def SetXPosition(self, value):
    if value > 10000:
      self.XPosition += 10000
    elif value < 0:
      self.XPosition += 0
    else:
      self.XPosition += value

  def SetYPosition(self, value):
    if value > 10000:
      self.YPosition += 10000
    elif value < 0:
      self.YPosition += 0
    else:
      self.YPosition += value

  def Move(self, cmd):
    if cmd == "up":
      self.YPosition += 10
    elif cmd == "down":
      self.YPosition -= 10
    elif cmd == "left":
      self.XPosition -= 10
    elif cmd == "right":
      self.XPosition += 10  
    else:
      print("Enter a valid command")

Jack = Character("Jack", 50, 50)


class BikeCharacter(Character):
  def __init__(self, Name, XPosition, YPosition):
    self.Name = Name # of data type STRING
    self.XPosition = XPosition # of data type INTEGER
    self.YPosition = YPosition # of data type INTEGER

  def Move(self, cmd):
    if cmd == "up":
      self.YPosition += 20
    elif cmd == "down":
      self.YPosition -= 20
    elif cmd == "left":
      self.XPosition -= 20
    elif cmd == "right":
      self.XPosition += 20  
    else:
      print("Enter a valid command")

Karla = BikeCharacter("Karla", 100, 50)

while True:
  char = str(input("Which character would you like to move?  "))
  if char.lower() == "jack" or char == "karla":
    break
  else:
    print("Enter a valid character")

while True:
  direction = str(input("In which direction would you them to move?  "))
  if direction.lower() == "up" or direction == "down" or direction == "left" or direction == "right":
    break
  else:
    print("Enter a valid direction")

if char == Jack.Name.lower():
  Jack.Move(direction)
  print(f"Jack's new position is X = {Jack.GetXPosition()} and Y = {Jack.GetYPosition()}")
elif char == Karla.Name.lower():
  Karla.Move(direction)
  print(f"Karla's new position is X = {Karla.GetXPosition()} and Y = {Karla.GetYPosition()}")
  