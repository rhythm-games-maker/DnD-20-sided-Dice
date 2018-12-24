from graphics import *
from random import randint

class Dice:
    def __init__(self, x = 200, y = 200):
        self.position = Point(x,y)
        self.numberPosition = Point(x-3, x-7)
        self.image = 'dice.png'
        self.number = ''
        self.dice = Image(self.position, self.image)
        self.luckyNumber = Text(self.numberPosition, self.number)

    def create(self, wn):
        self.luckyNumber.setSize(20)
        self.luckyNumber.setFill(color_rgb(255, 0, 0))
        self.luckyNumber.draw(wn)
        self.dice.draw(wn)
        return

    def roll(self):
        randNum = randint(1,20)
        self.number = str(randNum)
        return

    def set(self):
        self.luckyNumber.setText(self.number)
        return
    
class Button:
    def __init__(self):
        self.x = 200
        self.y = 325
        self.image = 'rollBtn.png'
        self.button = Image(Point(self.x,self.y), self.image)
        self.text = Text(Point(self.x,self.y), 'ROLL')
        return

    def create(self, wn):
        self.button.draw(wn)
        self.text.setFill(color_rgb(255,255,255))
        self.text.draw(wn)
        return

    def collide(self,wn):
        mouse = wn.getMouse()
        dx = abs(self.x - mouse.x)
        dy = abs(self.y - mouse.y)
        if dx < 40 and dy < 30:
            return True
        
def main():
    width = 400
    height = 400
    name = '20-Sided Dice'

    wn = GraphWin(name, width,height)
    
    myDice = Dice()
    myDice.create(wn)

    rollBtn = Button()
    rollBtn.create(wn)
    
    while True:
        torf = rollBtn.collide(wn)
        if torf == True:
            myDice.roll()
            myDice.set()
main()
