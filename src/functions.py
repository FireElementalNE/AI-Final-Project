import sys,os,random,time,trees,pickle # Imports
from random import randint
from config import *
from player import Player
from enemies import *

# this function print a newline
def endofLine(): 
    sys.stdout.write('\n')

# this function clears the screen
def clearScreen(): # depending on the OS the clear command might be different
    command = ''
    if myOS == 'Windows': # if windows
        command = 'cls'
    else: # if something else
        command = 'clear'
    os.system(command)

# this function handles the output for bad inputs
def tryAgain(): # if bad input
    clearScreen()
    print 'please try again'

# this function saves a game
def saveGame(allEnemies,thePlayer): # save the game
    enemiesfh = open('enemies','w+') # open files
    playerfh = open('player','w+')
    pickle.dump(allEnemies,enemiesfh) # save data
    pickle.dump(thePlayer,playerfh)
    enemiesfh.close() # close files
    playerfh.close()

# this function load a game and returns the allEnemies and thePlayer entities
def loadGame(): # load a game
    enemiesfh = open('enemies','r') # open files
    playerfh = open('player','r')
    enemyData = enemiesfh.read() # read files
    playerData = playerfh.read()
    allEnemies = pickle.loads(enemyData) # load pickle data for enemies
    thePlayer = pickle.loads(playerData) # load pickle data for player
    enemiesfh.close()
    playerfh.close()
    return [allEnemies,thePlayer] # return data

# this function removes all buffs from the player
def resetPlayer(thePlayer): # remove player defend buff
	thePlayer.currentDefence = thePlayer.defence
	return thePlayer

# this function attacks an entity, returning the defender after the attack and the damage dealt
def AttackEnemy(attacker,defender): # attack an entity
	lowerBound = int(attacker.currentAttack * LOWER_BOUND_ATTACK_DAMAGE) # bounds for damage
	upperBound = int(attacker.currentAttack * UPPER_BOUND_ATTACK_DAMAGE)
	baseDamage = randint(lowerBound,upperBound) # get a base damage numberr
	ar = armorReduction(defender.currentDefence) # get armor reduction percentage
	trueDamage = int(baseDamage * ar) # get the true damage
	defender.currentHP = defender.currentHP - trueDamage
	return [defender,trueDamage]

# this function constitues an attack, returning the Player class and the Enemies class after the attack move
def Attack(attacker,defender,allEnemies,playerAttack):
	if playerAttack: # if the player is attacking an enemy
		doubleAttack = randint(1,100) <= attacker.doubleSwing # calculate double swing chance
		dodge = randint(1,100) <= defender.dodge # calculate dodge change for the defender
		hit = randint(1,100) <= attacker.hit # calculate hit chance for the player
		if dodge or not hit: # if you missed or they dodged nothing happends to the defender
			print 'You attacked ' + defender.enemyType + ' and Missed!!'
		else:
			enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender) # otherwise you attack
			print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
			allEnemies.updateEnemey(enemyAfterAttack)
		if doubleAttack: # if a double attack attack again
			print 'Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge # calculate dodge change for the player
			hit = randint(1,100) <= attacker.hit # calculate hit chance for the player
			if dodge or not hit:
				print 'You attacked ' + defender.enemyType + ' and Missed!!'
			else: # you attack again!
				enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender)
				print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
				allEnemies.updateEnemey(enemyAfterAttack)
		return [attacker,allEnemies]
	else: # if the enemy is attacking the player
		playerAfterAttack = defender
		doubleAttack = randint(1,100) <= attacker.doubleSwing # calculate double swing chance
		dodge = randint(1,100) <= defender.dodge  # calculate dodge change for the player
		hit = randint(1,100) <= attacker.hit # calculate hit chance for the enemy
		if dodge or not hit:  # if enemy missed or they dodged nothing happends to the player
			print attacker.enemyType + ' attacked You and Missed!!'
		else:
			playerAfterAttack,dmgDone = AttackEnemy(attacker,defender) # otherwise enemy attacks
			print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!'
		if doubleAttack: # if a double attack attack again
			print 'Enemy Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge # calculate dodge change for the player
			hit = randint(1,100) <= attacker.hit # calculate hit chance for the player
			if dodge or not hit:  # if enemy missed or they dodged nothing happends to the player
				print attacker.enemyType + ' attacked You and Missed!!'
			else:
				playerAfterAttack,dmgDone = AttackEnemy(attacker,defender) # otherwise enemy attacks
				print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!' 
		return [playerAfterAttack,allEnemies] # return entities

# this function is for an entity that is defending, returns the entity after the defend
def Defend(el,playerDefend): 
	printString = ''
	healAmount = 0
	defenceBonus = 0
	healingBonus = 0
	if playerDefend: # if it is the player that is defending
		printString = 'You'
		defenceBonus = PLAYER_DEFENCE_BONUS
		healingBonus = PLAYER_HEALING_BONUS
	else: # if it is an enemy that is defending
		printString = el.enemyType
		defenceBonus = ENEMY_DEFENCE_BONUS
		healingBonus = ENEMY_HEALING_BONUS
	el.currentDefence = el.currentDefence * defenceBonus # defend!
	if el.currentHP >= (el.hitPoints * 1 - healingBonus): # heal the entity, if close to max hp heal to max hp
		healAmount = el.hitPoints - el.currentHP 
		el.currentHP = el.hitPoints
	else: # otherwise heal the heal amount
		healAmount = int(el.hitPoints * healingBonus)
		el.currentHP = el.currentHP + int(el.hitPoints * healingBonus)
	print printString + ' Defended! New Armor: ' + str(el.currentDefence) + '! Healed for ' + str(healAmount) + '!' # pretty printing! :D
	return el # rreturn entity

# this funtion heals an enemy (called by DEC), returns the source and target entities
def Heal(source,target):
	actualHeal = 0 # the actual amount to heal
	if target.hitPoints - target.currentHP < int(target.hitPoints * HEALAMOUNT): # if close to max hp heal to max hp
		actualHeal = target.hitPoints - target.currentHP
		target.currentHP = target.hitPoints
	else: # otherwise heal the heal amount
		target.currentHP = target.currentHP + int(target.hitPoints * HEALAMOUNT)
		actualHeal = int(target.hitPoints * HEALAMOUNT)
	print source.enemyType + ' Healed ' + target.enemyType + ' for ' + str(actualHeal) # pretty printing! :D
	source.currentMP = source.currentMP - HEALCOST # reduce enemy mp
	return [source,target] # return source and target entities

# this funtion casts Fireball, returns the Player class and the souce that cast the spell (a DEW)
def FireBall(source,thePlayer):
	baseDamage = FIREBALL_DAMAGE # get base damage
	ar = armorReduction(thePlayer.currentDefence) # get armorr reduction
	trueDamage = int(baseDamage * ar) # get true damage
	thePlayer.currentHP = thePlayer.currentHP - trueDamage # deal damage to player
	source.currentMP = source.currentMP - FIREBALL_COST # reduce enemy MP
	print source.enemyType + ' Cast FireBall and Dealt ' + str(trueDamage) + ' Damage!' # pretty printing! :D
	return [source,thePlayer] # return source and target entities

# this funtion casts Fireball, returns the enemy that it was cast on and the souce that cast the spell (a DEW)
def Buff(source,target):
	source.currentMP = source.currentMP - ATTACK_BUFF_COST # reduce MP
	target.currentAttack = int(target.currentAttack * ATTACK_BUFF_AMOUNT) # buff attack
	print source.enemyType + ' Buffed ' + target.enemyType +'\'s attack! New Attack: ' + str(target.currentAttack)  # print
	return [source,target] # return source and target entities

# this function takes the enemy turn, returning the playerr and allEnemies variables after the turn is complete
def enemyTurn(thePlayer,allEnemies):
	allEnemies.state.updateState(allEnemies) # update FSM
	for x in allEnemies.backRow: # start with back row so buffs will work
		backRowTree = None
		if x.enemyType == 'Dark Elf Archer': # if DEA
			backRowTree = trees.ArcherTree(x,thePlayer,allEnemies.state.currentState) # consult tree for action
			mAction = backRowTree.action # get action
			if mAction == 'Attack': # attack action
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x) # update enemy 
			elif mAction == 'Defend': # defend action
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x) # update enemy 
		elif x.enemyType == 'Dark Elf Cleric': # if DEC
			backRowTree = trees.ClericTree(x,allEnemies,thePlayer,allEnemies.state.currentState) # consult tree for action
			mAction,mTarget = backRowTree.action # get action and potential target to heal
			if mAction == 'Attack': # attack action
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x) # update enemy 
			elif mAction == 'Defend': # defend action
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x) # update enemy 
			elif mAction == 'Heal': # heal action
				x.status = 'Healing'
				x,target = Heal(x,mTarget)
				allEnemies.updateEnemey(x) # update enemy 
				allEnemies.updateEnemey(target) # update enemy that was healed
		elif x.enemyType == 'Dark Elf Wizard': # if DEW
			backRowTree = trees.WizardTree(x,allEnemies,thePlayer,allEnemies.state.currentState) # consult tree for action
			mAction,mTarget = backRowTree.action # get action and potential target to buff
			if mAction == 'Attack': # attack action
				thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
				x.status = 'Attacking'
				allEnemies.updateEnemey(x) # update enemy 
			elif mAction == 'Defend': # defend action
				x.status = 'Defending'
				x = Defend(x,False)
				allEnemies.updateEnemey(x) # cast fireball
			elif mAction == 'FireBall':
				x.status = 'Cast FireBall'
				x,thePlayer = FireBall(x,thePlayer) # cast fireball on player
				allEnemies.updateEnemey(x) # update enemy 
			elif mAction == 'AttackBuff': # buff action
				x.status = 'Buffing Ally'
				x,target = Buff(x,mTarget)
				allEnemies.updateEnemey(x) # update enemy 
				allEnemies.updateEnemey(target) # update enemy that was buffed
	for x in allEnemies.frontRow:
		frontRowTree = trees.OrcFighterTree(x,thePlayer,allEnemies.state.currentState)
		mAction = frontRowTree.action
		if mAction == 'Attack': # attack action
			thePlayer,allEnemies = Attack(x,thePlayer,allEnemies,False)
			x.status = 'Attacking'
			allEnemies.updateEnemey(x) # update enemy 
		elif mAction == 'Defend': # defend action
			x.status = 'Defending'
			x = Defend(x,False)
			allEnemies.updateEnemey(x) # update enemy 
	return [thePlayer,allEnemies] # return entities after the enemy turn

if __name__ == "__main__": # cannot call directly
	print 'This file, ' + sys.argv[0] + ', is only for import....'
	print 'to Play the game please run main.py:'
	print 'usage: python main.py'