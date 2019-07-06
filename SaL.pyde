



# My dice rolling sound does not work

def setup():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, startFill, startSquareX, startSquareY
    global backdrop, banner, dice, RandomDice, diceSound, numTiles, player1, track, distanceP1, distanceP2, tileBounds
    tileBounds = [-1]
    numTiles = 30
    allBoundaries = []
    startSquareX = 600
    startSquareY = 400
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 100
    squareWidth = 100
    numSquares = 1
    startFill = 20
    whichSquare = -1
    banner = loadImage("banner.png")
    backdrop = loadImage("snakes.png")
    dice = loadImage("dice.png")
    add_library('minim')
    minim=Minim(this)
    diceSound=minim.loadFile("DiceSound.mp3")
    size ( 700, 500 )
    RandomDice = int(random(0,6))
    player1 = False
    distanceP1 = 1
    distanceP2 = 1
    track = [i for i in range(numTiles+1)]
    track[3] = 22
    track[5] = 8
    track[11] = 26
    track[17] = 4
    track[19] = 7
    track[20] = 29
    track[21] = 9
    track[27] = 1
    for i in range( numSquares ):
        upperLeft =  [ squareXShow, squareYShow ]
        lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        squareXShow = squareXShow + squareWidth
    
    squareXShow = 0
    squareYShow = 400
    squareWidth = 100
    squareHeight = 100
    squareIncrease = 100 
    for i in range(5):
        for j in range(6):
            upperLeft = [ squareXShow, squareYShow ]
            lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
            clickBoundary = [ upperLeft, lowerRight ]
            tileBounds.append( clickBoundary )
            squareXShow = squareXShow + squareIncrease
        squareYShow -= squareHeight
        squareIncrease *= -1
        squareXShow += squareIncrease # So that when moving up rows it remains in the grid       
#    activeSquares[ 4 ] = False                  These just show what happened
#    print ( activeSquares )
            
#    print ( allboundaries )
#    print ( allboundaries[ 1 ])
#    print ( allboundaries[ 1 ][1])
#    print ( allboundaries[ 1 ][1][0] )
    
    
        
    
    
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares, RandomDice, diceSound, player1, distanceP1, distanceP2, track
    
#  all Boundaries is a list of tuples,  each tuple is the upper left and lower right of each box
#  if removeSquare is True, you will not be able to click again in that square again as that place in activeSquares will be turned to False
    whichSquare = - 1
    keepGoing = False
    for i in range( numSquares ):
        validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
        validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            whichSquare = i
            keepGoing = True
            break
    if keepGoing:
        if validLocation:
            player1 = not(player1)
            RandomDice = int(random(0,6))
            diceSound.play()
            delay(1000)
            diceSound.pause()
            diceSound.rewind()
            if player1:
                distanceP1 = track[RandomDice+1 + distanceP1]
            else:
                distanceP2 = track[RandomDice+1 + distanceP2]
    print(distanceP1, distanceP2)
    

def draw():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global backdrop, banner, dice, RandomDice, diceSound, distanceP1, distanceP2, tileBounds
   

    image(backdrop, 0, 0, 600, 500)
    image(banner, 600, 0, 100, 400, 10, 10, 110, 380)
    fill(255)
    rect( 600, 400, 100, 100)
    image(dice, 600, 400, 100, 100, 100*RandomDice, 0, 100+100*RandomDice, 97)
    strokeWeight(5)
    fill(255, 0, 0)
    ellipse(tileBounds[distanceP1][0][0] + 50, tileBounds[distanceP1][0][1] + 30, 20, 20)
    print(tileBounds[distanceP1][0][0], tileBounds[distanceP1][0][1])
    fill(0, 0, 255)
    ellipse(50+100*distanceP2, 470, 20, 20)    
        
        
        
