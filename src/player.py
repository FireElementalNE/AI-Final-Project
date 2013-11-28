from sys import stdout
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
    def __init__(self, CharacterType):
        self.name = CharacterType
        if CharacterType == 'Fighter':
            self.hitPoints = 710
            self.attack = 90
            self.defence = 80
            self.dodge = 5
            self.hit = 60
            self.doubleSwing = 15
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
        elif CharacterType == 'Wizard':
            self.hitPoints = 370
            self.attack = 120
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 5
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
        elif CharacterType == 'Thief':
            self.hitPoints = 500
            self.attack = 65
            self.defence = 60
            self.dodge = 30
            self.hit = 80
            self.doubleSwing = 40
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
    def printInfo(self,indent=''):
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
        stdout.write('PLAYER ' + '\n--------------\nClass: ' + str(self.name) + ' HP:' + str(self.currentHP) + '\n')
