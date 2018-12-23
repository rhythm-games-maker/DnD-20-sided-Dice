from graphics import *
from random import randint

wn = GraphWin('DnD Dice Generator', 400,400)

class MainDice:
    def __init__(self):
        self.position = Point(200,130)
        self.image = Image(self.position, 'dice.png')
        return

    def create(self, wn):
        self.image.draw(wn)
        return


class luckyNum():
    def __init__(self, text):
        self.text = text
        self.position = Point(197, 122)
        self.numberTxt = Text(self.position, self.text)

    def create(self, wn):
        self.numberTxt.setSize(20)
        self.numberTxt.setFill(color_rgb(255,0,0))
        self.numberTxt.draw(wn)
        return

    def destroy(self):
        self.numberTxt.undraw()
        return  

def randomNum():
    rand = randint(1,20)
    num = str(rand)
    return num


def main():
    global time    
    mydice = MainDice()
    mydice.create(wn)

    clickTxt = Text(Point(200,300), "Click to roll dice.")
    clickTxt.setSize(22)
    clickTxt.draw(wn)
    
    while True:
        mouse = wn.getMouse()
        num = randomNum()
        
        if mouse:
            myNum = luckyNum(num)
            myNum.create(wn)
            
            unclickTxt = Text(Point(200,350), "Click again to erase!")
            unclickTxt.setSize(18)
            unclickTxt.draw(wn)
            
            mouse = wn.getMouse()
            if mouse:
               myNum.destroy()
               unclickTxt.undraw()
main()
