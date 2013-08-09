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

  def turn(self): # how the queue must react to a new turn

    # Brew the beer
    for i in range(len(self.queue)):
      self.queue[i][1] -= 1

    self.inventory.extend([wort[0] for wort in self.queue 
                          if wort[1] == 0])
    self.queue = [wort for wort in self.queue if wort[1] != 0]

  def brew(self,beer,quantity):
    if beer.hops * quantity> self.hops:
        print "not enough hops"
        return False
    if beer.malt * quantity> self.malt:
        print "not enough malt"
        return False
    else:
        self.hops -= beer.hops
        self.malt -= beer.malt
        
        for _ in range(quantity):
          self.queue.append([beer,beer.turns+1])
        return True
          
  def buyHops(self, hopsQuantity, hopsPrice):
        totalPrice = hopsQuantity * hopsPrice
        print str(totalPrice)
        print str(self.cash)

        if  totalPrice > self.cash:
            print "not enough cash"
            return False
        else:
            self.hops += hopsQuantity
            self.cash -= totalPrice 
            return True

  def buyMalt(self, maltQuantity, maltPrice):
        totalPrice = maltQuantity * maltPrice
        if  totalPrice > self.cash:
            print "not enough cash"
            return False
        else:
            self.malt += maltQuantity
            self.cash -= totalPrice 
            return True

