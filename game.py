from beer import Beer
from player import Player
from gui import printGUI
from parser import Parser

import sys
           # name hops malt turns
beer = Beer('IPA',15,10,2)
beer2 = Beer('Bud',1,1,4)
beer3 = Beer('Dubble',1,1,4)

beers = [beer,beer2,beer3]

player = Player('Mike',1000,100,1000,[],[])
parser = Parser(player,beers)

beerPrices = {'IPA':50,'Bud':10,'Dubble':50}
resourcePrices = {'hops':10,'malt':2 }

def buy(noun,quantity):
    if noun == 'hops':
      player.buyHops(quantity,resourcePrices['hops'])
    elif noun == 'malt':
      player.buyMalt(quantity,resourcePrices['malt'])
    else:
        print "that's not for sale"

def getBeer(noun):
    for beer in beers:
        if noun == beer.name.lower():
            return beer
while 1:
  player.turn()
  printGUI(player)
  words = parser.parse(raw_input('>'))
  
  verb = words['verb']
  noun = words['noun']
  quantity = int(words['quantity'])

  del words

  if verb == 'exit':
      sys.exit()
  elif verb == 'buy':
      buy(noun,quantity)
  elif verb == 'brew':
      if noun in [beer.name.lower() for beer in beers]:
        player.brew(getBeer(noun),quantity)
      else:
          print "can't brew that"
  else:
      "didn't understand that"

