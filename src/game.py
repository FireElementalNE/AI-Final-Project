import sys,os,random,time
from config import *
from player import Player
from enemies import Enemies
#p1 = Player('Fighter')
#p2 = Player('Wizard')
#p3 = Player('Thief')
#e1 = Enemies('HOF',1)
#e2 = Enemies('LOF',2)
#e3 = Enemies('DEW',3)
#e4 = Enemies('DEC',4)
#e5 = Enemies('DEA',5)

playerClasses = ['Fighter', 'Wizard', 'Thief']
enemyClasses = ['HOF','LOF','DEW','DEC','DEA']
frontRowPossibilities = ['HOF','LOF']
backRowPossibilities = ['DEW','DEC','DEA']
commandPossibilities = ['Attack', 'Exit']

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

clearScreen()
print 'Welcome to AI Battle!'
print '------------------------------------------'
print 'Please pick your player class! (pick number NOT name)'
while True:

    for i in range(len(playerClasses)):
        print '[' + str(i)+ ']:' + ' ' + playerClasses[i]
    try:
        playerClassChoice = 0#int(raw_input('>'))
        if playerClassChoice >= 0 and playerClassChoice <= len(playerClasses):
            break
        else:
            raise ValueError
    except ValueError:
        print 'Incorrect Choice! Please Try again!'

thePlayer = Player(playerClasses[i])
thePlayer.printInfo()
enemyRow1 = []
enemyRow2 = []
print 'How many enemies do you want to fight?'
while True:
    try:
        enemyCount = 5#int(raw_input('>'))
        break
    except ValueError:
        continue

frontRowCount = (enemyCount / 2) + 1
backRowCount = enemyCount - frontRowCount

print 'FRONT ROW COUNT: ' + str(frontRowCount) + ' BACK ROW COUNT: ' + str(backRowCount)

print 'Picking Enemies!'

frontRow = []
backRow = []

for i in range(frontRowCount):
    tempEnemyIndex = random.randint(0,len(frontRowPossibilities)-1)
    frontRow.append(Enemies(frontRowPossibilities[tempEnemyIndex],i))
for i in range(backRowCount):
    tempEnemyIndex = random.randint(0,len(backRowPossibilities)-1)
    backRow.append(Enemies(backRowPossibilities[tempEnemyIndex],i+len(frontRow)))

print frontRow
print backRow


#clearScreen()

sys.stdout.write('Starting Game!')
#time.sleep(1)
sys.stdout.write('.')
#time.sleep(1)
sys.stdout.write('.')
#time.sleep(1)
sys.stdout.write('.')
endofLine()
command = ''
allEnemies = frontRow + backRow

while command.lower() not in exitStrings:
    print '-------------FRONT ROW--------------'
    for x in frontRow:
        sys.stdout.write('ID: ' + str(x.enemyId) + ' Type:' + str(x.enemyType) + ' HP:' + str(x.hitPoints) + '\n')
    endofLine()
    print '-------------BACK ROW---------------'
    for x in backRow: 
        sys.stdout.write('ID: ' + str(x.enemyId) + ' Type:' + str(x.enemyType) + ' HP:' + str(x.hitPoints) + '\n')

    print 'Commands!'
    for i in range(len(commandPossibilities)):
        print '[' + str(i) + '] ' + commandPossibilities[i]
    try:
        command = int(raw_input('>'))
        if command >= len(commandPossibilities) or command < 0:
            raise ValueError
    except ValueError:
        tryAgain()
        continue
    command = commandPossibilities[command]
    if  command == 'Attack':
        print 'Attack Who?'
        for x in allEnemies:
            print '[' + str(x.enemyId) + '] ' + x.enemyType
        try:
            enemyToAttack = int(raw_input('>'))
            if enemyToAttack >= len(allEnemies) or enemyToAttack < 0:
                raise ValueError
        except ValueError:
            tryAgain()
            continue
        enemyToAttack = allEnemies[enemyToAttack]
        
    
    command = 'e'

