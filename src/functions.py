import sys,os,random,time,trees
from random import randint
from config import *
from player import Player
from enemies import *


def endofLine():
    sys.stdout.write('\n')

def clearScreen():
    command = ''
    if myOS == 'Windows':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

def tryAgain():
    clearScreen()
    print 'please try again'

def resetPlayer(thePlayer):
	thePlayer.currentDefence = thePlayer.defence
	return thePlayer

def AttackEnemy(attacker,defender):
	lowerBound = int(attacker.currentAttack * LOWER_BOUND_ATTACK_DAMAGE)
	upperBound = int(attacker.currentAttack * UPPER_BOUND_ATTACK_DAMAGE)
	baseDamage = randint(lowerBound,upperBound)
	ar = armorReduction(defender.currentDefence)
	trueDamage = int(baseDamage * ar)
	defender.currentHP = defender.currentHP - trueDamage
	return [defender,trueDamage]


def Attack(attacker,defender,allEnemies,playerAttack):
	if playerAttack:
		doubleAttack = randint(1,100) <= attacker.doubleSwing
		dodge = randint(1,100) <= defender.dodge
		if dodge:
			print 'You attacked ' + defender.enemyType + ' and Missed!!'
		else:
			enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender)
			print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
			allEnemies.updateEnemey(enemyAfterAttack)
		if doubleAttack:
			print 'Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge
			if dodge:
				print 'You attacked ' + defender.enemyType + ' and Missed!!'
			else:
				doubleAttackChance = randint(1,100)
				doubleAttack = doubleAttackChance <= attacker.doubleSwing
				enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender)
				print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
				allEnemies.updateEnemey(enemyAfterAttack)
		return [attacker,allEnemies]
	else:
		playerAfterAttack = defender
		doubleAttack = randint(1,100) <= attacker.doubleSwing
		dodge = randint(1,100) <= defender.dodge
		if dodge:
			print attacker.enemyType + ' attacked You and Missed!!'
		else:
			playerAfterAttack,dmgDone = AttackEnemy(attacker,defender)
			print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!'
		if doubleAttack:
			print 'Enemy Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge
			if dodge:
				print attacker.enemyType + ' attacked You and Missed!!'
			else:
				playerAfterAttack,dmgDone = AttackEnemy(attacker,defender)
				print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!'
		return [playerAfterAttack,allEnemies]

def Defend(el,playerDefend):
	printString = ''
	healAmount = 0
	defenceBonus = 0
	healingBonus = 0
	if playerDefend:
		printString = 'You'
		defenceBonus = PLAYER_DEFENCE_BONUS
		healingBonus = PLAYER_HEALING_BONUS
	else:
		printString = el.enemyType
		defenceBonus = ENEMY_DEFENCE_BONUS
		healingBonus = ENEMY_HEALING_BONUS
	el.currentDefence = el.currentDefence * defenceBonus
	if el.currentHP >= (el.hitPoints * 1 - healingBonus):
		healAmount = el.hitPoints - el.currentHP
		el.currentHP = el.hitPoints
	else:
		healAmount = int(el.hitPoints * healingBonus)
		el.currentHP = el.currentHP + int(el.hitPoints * healingBonus)
	print printString + ' Defended! New Armor: ' + str(el.currentDefence) + '! Healed for ' + str(healAmount) + '!'
	return el

def Heal(source,target):
	actualHeal = 0
	if target.hitPoints - target.currentHP < int(target.hitPoints * HEALAMOUNT):
		actualHeal = target.hitPoints - target.currentHP
		target.currentHP = target.hitPoints
	else:
		target.currentHP = target.currentHP + int(target.hitPoints * HEALAMOUNT)
		actualHeal = int(target.hitPoints * HEALAMOUNT)
	print source.enemyType + ' Healed ' + target.enemyType + ' for ' + str(actualHeal)
	source.currentMP = source.currentMP - HEALCOST
	return [source,target]

def FireBall(source,thePlayer):
	baseDamage = FIREBALL_DAMAGE
	ar = armorReduction(thePlayer.currentDefence)
	trueDamage = int(baseDamage * ar)
	thePlayer.currentHP = thePlayer.currentHP - trueDamage
	source.currentMP = source.currentMP - FIREBALL_COST
	print source.enemyType + ' Cast FireBall and Dealt ' + str(trueDamage) + ' Damage!'
	return [source,thePlayer]

def Buff(source,target):
	source.currentMP = source.currentMP - ATTACK_BUFF_COST
	target.currentAttack = int(target.currentAttack * ATTACK_BUFF_AMOUNT)
	print source.enemyType + ' Buffed ' + target.enemyType +'\'s attack! New Attack: ' + str(target.currentAttack)
	return [source,target]

def enemyTurn(thePlayer,allEnemies):
	allEnemies.state.updateState(allEnemies)
	for x in allEnemies.frontRow:
		frontRowTree = trees.OrcFighterTree(x,thePlayer,allEnemies.state.currentState)
		mAction = frontRowTree.action
		if mAction == 'Attack':
			thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
			x.status = 'Attacking'
			allEnemies.updateEnemey(x)
		elif mAction == 'Defend':
			x.status = 'Defending'
			x = Defend(x,False)
			allEnemies.updateEnemey(x)
	for x in allEnemies.backRow:
		backRowTree = None
		if x.enemyType == 'Dark Elf Archer':
			backRowTree = trees.ArcherTree(x,thePlayer,allEnemies.state.currentState)
			mAction = backRowTree.action
			if mAction == 'Attack':
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x)
			elif mAction == 'Defend':
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x)
		elif x.enemyType == 'Dark Elf Cleric':
			backRowTree = trees.ClericTree(x,allEnemies,thePlayer,allEnemies.state.currentState)
			mAction,mTarget = backRowTree.action
			if mAction == 'Attack':
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x)
			elif mAction == 'Defend':
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x)
			elif mAction == 'Heal':
				x.status = 'Healing'
				x,target = Heal(x,mTarget)
				allEnemies.updateEnemey(x)
				allEnemies.updateEnemey(target)
		elif x.enemyType == 'Dark Elf Wizard':
			backRowTree = trees.WizardTree(x,allEnemies,thePlayer,allEnemies.state.currentState)
			mAction,mTarget = backRowTree.action
			if mAction == 'Attack':
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x)
			elif mAction == 'Defend':
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x)
			elif mAction == 'FireBall':
				x.status = 'Cast FireBall'
				x,thePlayer = FireBall(x,thePlayer)
				allEnemies.updateEnemey(x)
			elif mAction == 'AttackBuff':
				x.status = 'Buffing Ally'
				x,target = Buff(x,mTarget)
				allEnemies.updateEnemey(x)
				allEnemies.updateEnemey(target)


	return [thePlayer,allEnemies]	




