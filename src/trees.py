from player import Player
from enemies import Enemies

class OrcFighterTree:
	action = ''
	def __init__(self,of,theplayer):
		if of.currentHP < (0.7 * of.hitPoints):
			self.action = 'Defend'
		else:
			self.action = 'Attack'

