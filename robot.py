from random import randint

print('Here is a random number', randint(0,10))

start()
print('The console even works')

addHeading("You like giant robots!", 48)

score = 0
scoreText = addText(score, 48)
positionEl(scoreText, 100, 100)

laserSound = addSoundEffect('laser.mp3')

def addRobot():
    robot0 = addImage("robot.png", 100)
    positionEl(robot0, 100, 300)
    moveX(robot0, 100, 1100, "infinite", True)

addRobot()
addRobot()

def shoot(target):
    playMusic(laserSound)
    global score
    score = score + 1
    updateText(scoreText, score)
    if score == 4:
        addHeading("Finally an Ace", 20)
    elif score == 20:
        addHeading("For Zeon!", 20)
    elif score == 30:
        addHeading("Char would be proud", 20)
    elif score == 40:
        addHeading("Increadible!!!!", 20)
    # vanish(target)
    

for c in range(0, 40):
    zeon = addImage("zeon.png", 40)
    x = randomNum(100, 1000)
    y = randomNum(800, 1600)
    speed = randomNum(10, 30)
    positionEl(zeon, x, y)
    moveY(zeon, y, -100, 1, False, speed)
    zeon.click(zeon, shoot)
