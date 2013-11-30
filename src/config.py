import platform

def armorReduction(cd):
	return (((150 - cd) / 100.0) * 0.7)

MPTURN = 10
HEALCOST = 35
HEALAMOUNT = 0.10
FIREBALL_COST = 60
FIREBALL_DAMAGE = 110
ATTACK_BUFF_COST = 30
ATTACK_BUFF_AMOUNT = 1.15
BUFF_PROC = 30

FIGHTER_HEAL_THRESHHOLD = 0.7
ARCHER_HEAL_THRESHOLD = 0.75
PLAYER_DEFENCE_BONUS = 1.5
PLAYER_HEALING_BONUS = 0.1
ENEMY_DEFENCE_BONUS = 1.2
ENEMY_HEALING_BONUS = 0.06

LOWER_BOUND_ATTACK_DAMAGE = 0.7
UPPER_BOUND_ATTACK_DAMAGE = 1.5

myOS = platform.system()
exitStrings = ['e','exit','bye','quit']
