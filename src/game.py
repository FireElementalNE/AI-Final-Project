import sys,time,functions,getpass # Imports
from random import randint
from config import *
from player import Player
from enemies import *
from states import States

# runs the game
def runGame():
    playerClasses = ['Fighter', 'Thief'] # possible player classes
    enemyClasses = ['HOF','LOF','DEW','DEC','DEA'] # possible enemy classes (no used)
    frontRowPossibilities = ['HOF','LOF'] # possible front row enemy classes 
    backRowPossibilities = ['DEW','DEC','DEA'] # possible back row enemy classes 
    commandPossibilities = ['Attack','Defend', 'Save', 'Exit'] # player actions

    functions.clearScreen()
    print 'Welcome to AI Battle!'
    print '------------------------------------------'
    print 'Load Game?' # load a previous game?
    allEnemies = None
    thePlayer = None
    load = raw_input('(y/n)> ')
    if load.lower() in afermativeStrings:
        allEnemies,thePlayer = functions.loadGame() # load a saved game
    else:
        print 'Please pick your player class! (pick number NOT name)'
        while True: # used to pick player classes
            for i in range(len(playerClasses)):
                print '[' + str(i)+ ']:' + ' ' + playerClasses[i]
            try:
                playerClassChoice = int(raw_input('>'))
                if playerClassChoice >= 0 and playerClassChoice <= len(playerClasses):
                    break
                else:
                    raise ValueError
            except ValueError: # incorrect input
                print 'Incorrect Choice! Please Try again!'

        thePlayer = Player(playerClasses[playerClassChoice]) # init player
        thePlayer.printInfo()

        print 'How many enemies do you want to fight?'
        while True: # used to pick numbers of enemies
            try:
                enemyCount = int(raw_input('>'))
                break
            except ValueError:
                continue

        frontRowCount = (enemyCount / 2) + 1 # there is always more front row enemies than back row enemies
        backRowCount = enemyCount - frontRowCount
        functions.endofLine()

        print 'Picking Enemies!'
        functions.endofLine()
        frontRow = [] # init front and back rows
        backRow = []

        for i in range(frontRowCount): # randomly pick front row enemies
            tempEnemyIndex = randint(0,len(frontRowPossibilities)-1)
            frontRow.append(Enemy(frontRowPossibilities[tempEnemyIndex],i))
        for i in range(backRowCount): # randomly pick back row enemies
            tempEnemyIndex = randint(0,len(backRowPossibilities)-1)
            backRow.append(Enemy(backRowPossibilities[tempEnemyIndex],i+len(frontRow)))

        initState = States('Attack!') # initialize enemey FSM
        allEnemies = Enemies(frontRow,backRow,initState) # create enemy team object

    sys.stdout.write('Starting Game!')
    functions.endofLine()
    command = ''
    functions.endofLine()
    while command.lower() not in exitStrings:
        if len(allEnemies.getAllEnemies()) <= 0: # winning condition
            print 'YOU WIN!'
            break;
        elif thePlayer.currentHP <= 0: # losing condition
            print 'YOU LOST!'
            break;
        wait = getpass.getpass('press enter key to continue...') # pauses game
        functions.clearScreen()
        thePlayer = functions.resetPlayer(thePlayer) # remove buffs and such fom playerr
        functions.endofLine() 
        allEnemies.printEnemies()
        functions.endofLine()
        thePlayer.printInfoLine()
        functions.endofLine()
        print 'Commands!'
        for i in range(len(commandPossibilities)): # print possible player commands
            print '[' + str(i) + '] ' + commandPossibilities[i]
        try:
            command = int(raw_input('>')) # pick command
            if command >= len(commandPossibilities) or command < 0:
                raise ValueError
        except ValueError: # error checking
            functions.tryAgain()
            continue
        functions.clearScreen()
        command = commandPossibilities[command]
        if  command == 'Attack': # attack command
            print 'Attack Who?' 
            for x in allEnemies.getAllEnemies(): # get target to attack
                print '[' + str(x.enemyId) + '] ' + x.enemyType
            try:
                enemyToAttackID = int(raw_input('>'))
                if not allEnemies.validId(enemyToAttackID):
                    raise ValueError
            except ValueError: # error checking
                functions.tryAgain()
                continue
            enemyToAttack = allEnemies.getEnemey(enemyToAttackID)
            thePlayer,allEnemies= functions.Attack(thePlayer,enemyToAttack,allEnemies,True)
        if command == 'Defend': # defend command
            thePlayer = functions.Defend(thePlayer,True)
            print 'You are Defending!'
            print 'current Stats:'
            thePlayer.printInfo('--> ')
        if command == 'Save': # save game using pickle
            functions.saveGame(allEnemies,thePlayer) # save the current game
            break
        if command.lower() not in exitStrings: # amke surre the user did not exit
            allEnemies.resetEnemies() # reset enemeies (rremove defence buffs and AttackBuff)
            allEnemies.removeDeadEnemeies() # RRemove the dead enemies
            functions.endofLine()
            functions.endofLine()
            thePlayer,allEnemies = functions.enemyTurn(thePlayer,allEnemies) # take the enemy turn
            functions.endofLine()

if __name__ == "__main__":
    runGame() # run the game