from graphics import *
from random import randint

class Dice:
    def __init__(self, x = 200, y = 200):
        self.position = Point(x,y)
        self.numberPosition = Point(197, 193)
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

def main():
    width = 400
    height = 400
    name = '20-Sided Dice'

    wn = GraphWin(name, width,height)

    myDice = Dice()
    myDice.create(wn)

    while True:
        mouse = wn.getMouse()
        if mouse:
            myDice.roll()
            myDice.set()
main()
