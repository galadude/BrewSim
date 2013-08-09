from beer import Beer
from player import Player
from gui import printGUI
from parser import Parser

           # name hops malt turns
beer = Beer('IPA',15,10,2)
beer2 = Beer('Bud',1,1,4)
beer3 = Beer('Dubble',1,1,4)

player = Player('Mike',1000,0,0,[],[])
parser = Parser(player,[beer,beer2,beer3])

beerPrices = {'IPA':50,'Bud':10,'Dubble':50}
resourcePrice = {'hops':10,'malt':2 }

while 1:
  words = parser.parse(raw_input('>'))

