from sys import stdout,argv
from config import *
# class forr a single enemy
class Enemy:
    enemyType = ''
    enemyId = ''
    hitPoints = 0
    attack = 0
    defence = 0
    dodge = 0.0
    hit = 0.0
    specials = []
    doubleSwing = 0
    state = None
    row = None
    currentDefence = 0
    currentHP = 0
    status = 'Nothing'
    magicPoints = 0
    currentMP = 0
    currentAttack = 0
    def __init__(self, EnemyType,ID):
        if EnemyType == 'HOF': # create HOF (see table 2)
            self.enemyType = 'Heavy Orc Fighter'
            self.enemyId = ID
            self.hitPoints = 300
            self.attack = 20
            self.defence = 80
            self.dodge = 5
            self.hit = 60
            self.doubleSwing = 5
            self.row = 1
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.currentAttack = self.attack
        elif EnemyType == 'LOF': # create LOF (see table 2)
            self.enemyType = 'Light Orc Figher'
            self.enemyId = ID
            self.hitPoints = 190
            self.attack = 27
            self.defence = 60
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 15
            self.row = 1
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.currentAttack = self.attack
        elif EnemyType == 'DEW': # create DEW (see table 2)
            self.enemyType = 'Dark Elf Wizard'
            self.enemyId = ID
            self.hitPoints = 140
            self.attack = 45
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 1
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.magicPoints = 100
            self.currentMP = self.magicPoints
            self.currentAttack = self.attack
        elif EnemyType == 'DEC': # create DEC (see table 2)
            self.enemyType = 'Dark Elf Cleric'
            self.enemyId = ID
            self.hitPoints = 140
            self.attack = 15
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doublewing = 5
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.magicPoints = 100
            self.currentMP = self.magicPoints
            self.currentAttack = self.attack
        elif EnemyType == 'DEA': # create DEA (see table 2)
            self.enemyType = 'Dark Elf Archer'
            self.enemyId = ID
            self.hitPoints = 170
            self.attack = 17
            self.defence = 50
            self.dodge = 30
            self.hit = 80
            self.doubleSwing = 20
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.currentAttack = self.attack
    def printInfo(self): # pretty printing
        print 'ID         = ' + str(self.enemyId)
        print 'Name       = ' + self.enemyType
        print 'Hit Points = ' + str(self.hitPoints)
        print 'Attack     = ' + str(self.attack)
        print 'Defence    = ' + str(self.defence)
        print 'Dodge      = ' + str(self.dodge) + '%'
        print 'Hit        = ' + str(self.hit) + '%'
        print 'DoubleHit  = ' + str(self.doubleSwing) + '%'
        print 'Row        = ' + str(self.row)
        print 'C Defence  = ' + str(self.currentDefence)
        print 'C HP       = ' + str(self.currentHP)
    def printInfoLine(self): # single line printing
         stdout.write('ID: ' + str(self.enemyId) + ' Type:' + str(self.enemyType) + ' HP:' + str(self.currentHP) + ' STATUS: ' + self.status + ' MP: ' + str(self.currentMP) + '\n')

# class for the enemy team
class Enemies:
    frontRow = [] # frront rrow
    backRow = [] # back row
    state = None # get state from FSM
    def __init__(self,fr,br,st): # init
        self.frontRow = fr
        self.backRow = br
        self.state = st

    # this funtion updates an enemy
    def updateEnemey(self,enemy): 
        if enemy.row == 1:
            for i in range(len(self.frontRow)):
                if self.frontRow[i] == enemy.enemyId:
                    self.frontRow[i] = enemy
        else:
            for i in range(len(self.backRow)):
                if self.backRow[i] == enemy.enemyId:
                    self.backRow[i] = enemy

    # this funtion chekcs to see if an id is valid
    def validId(self,mId):
        for x in self.frontRow:
            if x.enemyId == mId:
                return True
        for x in self.backRow:
            if x.enemyId == mId:
                return True
        return False

    # this funtion returns an enemy
    def getEnemey(self,mId):
        for x in self.frontRow:
            if x.enemyId == mId:
                return x
        for x in self.backRow:
            if x.enemyId == mId:
                return x

    # Pretty Prrinting!!!!
    def printEnemies(self):
        print 'ENEMY STATE: ' + self.state.currentState
        print '-------------FRONT ROW--------------'
        for x in self.frontRow:
            x.printInfoLine()
        stdout.write('\n')
        print '-------------BACK ROW---------------'
        for x in self.backRow: 
            x.printInfoLine()

    # this function uses HOFC to remove dead enemies
    def removeDeadEnemeies(self):
        self.frontRow = filter(lambda x: x.currentHP > 0, self.frontRow)
        self.backRow = filter(lambda x: x.currentHP > 0, self.backRow)

    # this funtion resets all enemies (removing buffs like AttackBuff orr Defence buff)
    def resetEnemies(self):
        for x in self.frontRow:
            x.currentDefence = x.defence
            x.currentAttack = x.attack
        for x in self.backRow:      
            x.currentDefence = x.defence
            x.currentAttack = x.attack
            if x.enemyType == 'Dark Elf Cleric' or x.enemyType == 'Dark Elf Wizard':
                if x.magicPoints - x.currentMP < MPTURN:
                    x.currentMP = x.magicPoints
                else:
                    x.currentMP = x.currentMP + MPTURN
                    
    # this funtion rreturns all enemies
    def getAllEnemies(self):
        return self.frontRow+self.backRow

if __name__ == "__main__": # cannot call directly
    print 'This file, ' + argv[0] + ', is only for import....'
    print 'to Play the game please run main.py:'
    print 'usage: python main.py'