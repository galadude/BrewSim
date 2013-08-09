from player import Player
from beer import Beer

def printGUI(player):
  print_resources(player)
  printQueue(player.queue)


def char_inserter(chr_length, char = " "):
  spaces = ""
  for row in range(0,chr_length):
     spaces += char
  return spaces

# List of strings for easy printing
def invPrintList(inv):
    beers = {}

    for beer in inv:
        if beer.name in beers.keys():
           beers[beer.name] += 1 
        else:
            beers[beer.name] = 1

    list = ["   INVENTORY"]

    for beer in beers:
      list.append(beer + ": " +  str(beers[beer]))
    return list

def printQueue(queue):
  title = "Queue"
  spaces = char_inserter((51-len(title))/2)

  print spaces + title + spaces
  print "8" + char_inserter(49,"-") + "8"
  beer_line = ""

  for wort in queue:
     turns = str(wort[0].turns-wort[1]+1)
     print "  " + wort[0].name + " " + turns + "/" + str(wort[0].turns)

def print_resources(player):
  title = "RESOURCES"
  spaces = char_inserter((51-len(title))/2)

  print spaces + title + spaces
  print "8" + char_inserter(49,"-") + "8"
  beer_line = ""

  inv = invPrintList(player.inventory)
  for row in range(max(3,len(inv))):
    if row <= len(inv)-1:
      beer_line =  inv[row]
    else:
        beer_line = ""
           
    # Prints resources
    other_line = ""
    if row == 0: other_line = "Malt: " + str(player.malt)
    if row == 1: other_line = "Hops: " + str(player.hops)
    if row == 2: other_line = "Cash: " + str(player.cash)

    spaces = char_inserter(49-len(beer_line)-len(other_line))
    
    print " " + beer_line + spaces + other_line

  print "8" + char_inserter(49,"-") + "8"

