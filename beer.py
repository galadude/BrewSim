'''

'''

class Beer:
  def __init__(self,name,hops,malt,turns):
    self.name = name
    self.hops = hops
    self.malt = malt
    self.turns = turns

  def __str__(self):
      return self.name

  def __repr__(self):
      return self.name
