'''
File: Player.py
Author: Michael Glen Galanakis
'''
from beer import Beer

class Player:
  def __init__(self,name,cash,hops,malt,inventory,queue):
    self.name = name
    self.cash = cash
    self.hops = hops
    self.malt = malt

    self.inventory = inventory # What beer we have at the moment
    self.queue = queue # beer busy being brewed

  def turn_queue(self): # how the queue must react to a new turn
    for wort in self.queue: 
        if wort[1] == 0:
            print wort[0].name
            self.inventory.append(wort[0])
        else:
          wort[1] -= 1
    for beer in self.inventory:
        print beer.name

  def brew(self,beer,quantity):
    if beer.hops * quantity> self.hops:
        print "not enough hops"
        return false
    if beer.malt * quantity> self.malt:
        print "not enough malt"
        return false
    else:
        self.hops -= beer.hops
        self.malt -= beer.malt
        
        for _ in range(quantity):
          self.queue.append([beer,beer.turns])
        return True

          

beer = Beer('IPA',2,5,2)

player = Player('Mike',1000,100,100,[],[])

player.brew(beer,3)
player.turn_queue()
player.turn_queue()


