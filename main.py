import pyautogui
##96 180 500 470 ##24 pixels = 1 block

global red, orange, blue, pink, lblue, green, yellow
red = (215, 15, 55)
orange = (227, 91, 2)
blue = (33, 65, 198)
pink = (175, 41, 138)
lblue = (15, 155, 215)
green = (89, 177, 1)
yellow = (227, 159, 2)

class fstris:
    def getColorOfPixel(self, x, y):
        global red, orange, blue, pink, lblue, green, yellow

        rgb = pyautogui.pixel(x, y) ##146, 225  54, 225
        
        if rgb == blue:
            return 0
        elif rgb == pink:
            return 1
        elif rgb == lblue:
            return 2
        elif rgb == orange:
            return 3
        elif rgb == red:
            return 4
        elif rgb == green:
            return 6
        elif rgb == yellow:
            return 7
        else:
            return 2

    def checkBoardSpaces(self):
        x = 237
        y = 187
        for a in range(0, 10):
            y += i * 24
            for i in range(0, 19):
                self.getColorOfPixel(x + i * 24, y)

    def ai(self):
        pyautogui.keyDown("alt")
    pyautogui.keyDown("tab")
    pyautogui.keyUp("alt")
    pyautogui.keyUp("tab")
    pyautogui.keyDown("c")
    pyautogui.keyUp("c")


game = fstris()

##start
game.ai()


##debug
###oldh, oldn0, oldn1 = (0, 0, 0)
###while True:
###    newh = game.getColorOfPixel(174, 227) ##held piece
###    if oldh != newh:
###        print("held: " + str(newh))
###    oldh = newh
###
###    newn0 = game.getColorOfPixel(543, 227) ##next in line 0
###    if oldc != newn0:
###        print("current: " + str(newn0))
###    oldc = newn0
###
###    newn1 = game.getColorOfPixel(543, 299) ##next in line 1
###    if oldn0 != newn1:
###        print("next: " + str(newn1))
###    oldn0 = newn1