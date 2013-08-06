import random
import sys

# The resources owned by the player
exit = False
money = 1000
hops = 0
malt = 0
beer = 0
production_slots = 10

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
inventory = [0,0,0]
	 
queue = [[]] # beer being brewed

def turn():
	generate_prices()

	new_queue = [[]]
	for [name,turns] in queue:
		new_queue.add([name,turns-1])
	queue = new_queue	

def brew(beer,quantity):
	for row in range(0,quantity):
		queue.add([beer.name,beer.turns])

def generate_prices():
	for price in prices:
		# I'd like this to run on a normal distribution instead
		rand_int = random.randrange(-1,1)		
		price += price * rand_int

def parse_command(cmd):
	cmd_lst = cmd.split(' ')
	global money
	global hops

	if cmd_lst[0] == 'exit':
		sys.exit()
	elif cmd_lst[0] == 'buy':
		if cmd_lst[1] == 'hops':
			try:
				quantity = int(cmd_lst[2])
			except:
				print "Insert valid quantity"
			cost = prices[1] * quantity
 			if money > cost:	
				money -= cost
				hops += quantity
				

def char_inserter(chr_length, char = " "):
	spaces = ""	
	for row in range(0,chr_length):
		spaces += char
	return spaces

# The row system needs fixing
def user_interface():
	for row in range(0,100):
		print ""
	print_resources()
	print_prices()

def print_resources():
	title = "RESOURCES"
	spaces = char_inserter((51-len(title))/2)

	print spaces + title + spaces
	print "8" + char_inserter(49,"-") + "8"

	for row in [0,1,2]:
	  beer_line = beers[row].name + ": " + str(inventory[row])
	  other_line = ""
	  if row == 0: other_line = "Malt: " + str(malt)
	  if row == 1: other_line = "Hops: " + str(hops)
	  if row == 2: other_line = "Cash: " + str(money)

	  spaces = char_inserter(49-len(beer_line)-len(other_line))
	  
	  print " " + beer_line + spaces + other_line

	print "8" + char_inserter(49,"-") + "8"

def print_prices():
	title = "PRICES"
	spaces = char_inserter((51-len(title))/2)

	print spaces + title + spaces
	print "8" + char_inserter(49,"-") + "8"
	
	for beer in beers:
		print " " + beer.name + ": " + str(beer.price)

	print "8" + char_inserter(49,"-") + "8"

	for i in range(0,len(prices)):
		print " " + str(products[i]) + ": " + str(prices[i])
	
def print_brewing():
	title = "BREW"
	spaces = char_inserter((51-len(title))/2)
	
	print " Slots: " + production_slots
	for beer in queue:
		print ""

def game_start(days):
	while True:
		user_interface()
		cmd = raw_input('( -.-) ')
		parse_command(cmd)
		
game_start(20)
