from sys import stdout,argv # imports
class Player:
    name = ''
    hitPoints = 0 
    attack = 0
    defence = 0
    dodge = 0.0
    hit = 0.0
    specials = []
    doubleSwing = 0
    currentDefence = 0
    currentAttack = 0
    def __init__(self, CharacterType):
        self.name = CharacterType
        if CharacterType == 'Fighter': # create fighter (see table 1)
            self.hitPoints = 710
            self.attack = 90
            self.defence = 75
            self.dodge = 5
            self.hit = 90
            self.doubleSwing = 15
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.currentAttack = self.attack
        elif CharacterType == 'Thief': # create Thief (see table 1)
            self.hitPoints = 500
            self.attack = 60
            self.defence = 55
            self.dodge = 30
            self.hit = 60
            self.doubleSwing = 40
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.currentAttack = self.attack
    def printInfo(self,indent=''): # pretty printing!!!! :D :D
        print indent + 'Class:     = ' + self.name
        print indent + 'Hit Points = ' + str(self.hitPoints)
        print indent + 'Attack     = ' + str(self.attack)
        print indent + 'Defence    = ' + str(self.defence)
        print indent + 'Dodge      = ' + str(self.dodge) + '%'
        print indent + 'Hit        = ' + str(self.hit) + '%'
        print indent + 'DoubleHit  = ' + str(self.doubleSwing) + '%'
        print indent + 'C Defence  = ' + str(self.currentDefence)
        print indent + 'C HP       = ' + str(self.currentHP)
    def printInfoLine(self):
        stdout.write('PLAYER ' + '\n--------------\nClass: ' + str(self.name) + ' HP:' + str(self.currentHP) + '\n') # single line printing

if __name__ == "__main__": # cannot call directly
    print 'This file, ' + argv[0] + ', is only for import....'
    print 'to Play the game please run main.py:'
    print 'usage: python main.py'