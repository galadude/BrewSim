'''
  Parsers commands from the user
'''
from beer import Beer

class Parser:
    def __init__(self,player,beers):
        self.beers = beers
        self.verbs = [
                     'buy', # Buy hops and malt
                     'sell', # Sell beer
                     'brew', # brew beer
                     'exit'
                     ]
        self.nouns = [
                     'hops',
                     'malt'
                     ]

    def addBeers(self,beers):
       for beer in beers:
           self.nouns.append(beer.name.lower())
    
    def parse(self,cmd):
        self.addBeers(self.beers)

        words = cmd.lower().split(' ')
    
        verb = ''
        noun = ''
        quantity =  0

        for word in words:
            if word in self.nouns:
                noun = word
            elif word in self.verbs:
                verb = word
            elif isNumber(word):
                quantity = (word)
        return {'verb':verb,'noun':noun,'quantity':quantity}



def isNumber(word):
    try:
        int(word)
        return True
    except ValueError:
        return False
        
        

    

