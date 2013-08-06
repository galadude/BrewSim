import random

# The resources owned by the player
money = 1000
hops = 0
malt = 0
beer = 0
production_level = 1

class Beer:
	def __init__(self,name,hops,malt,price,turns):
		self.name = name
		self.hops = hops
		self.malt = malt
		self.price = price 
		self.turns = turns # Turns until finished 

# The base price of hops and malt
prices = [2,5]
products = ['malt','hops']
beers = [
		Beer('Indian Pale Ale',5,5,60,4),
		Beer('Dubble',2,2,80,10),
		Beer('Generic Lager',1,1,15,2)
	]

	 
def generate_prices():
	for price in prices:
		# I'd like this to run on a normal distribution instead
		rand_int = random.randrange(-1,1)		
		price += price * rand_int

def produce_beer():
	hops -= 50 * production_level
	malt -= 100 * production_level
	beer += 100 * production_level

def parse_command(cmd):
	cmd_lst = cmd.split(' ')
	for word in cmd_lst:
		print word	
parse_command('asdf asdf asfd')
