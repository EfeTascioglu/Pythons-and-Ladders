



# My dice rolling sound does not work

def setup():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, startFill, startSquareX, startSquareY
    global backdrop, banner, dice, RandomDice, diceSound
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
    
    for i in range( numSquares ):
        upperLeft =  [ squareXShow, squareYShow ]
        lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        squareXShow = squareXShow + squareWidth
    print( allBoundaries )
    
#    activeSquares[ 4 ] = False                  These just show what happened
#    print ( activeSquares )
            
#    print ( allboundaries )
#    print ( allboundaries[ 1 ])
#    print ( allboundaries[ 1 ][1])
#    print ( allboundaries[ 1 ][1][0] )
    
    
        
    
    
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares, RandomDice, diceSound
    
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
            RandomDice = int(random(0,6))
            diceSound.play()
        
    

def draw():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global backdrop, banner, dice, RandomDice, diceSound
   

    image(backdrop, 0, 0, 600, 500)
    image(banner, 600, 0, 100, 400, 10, 10, 110, 380)
    fill(255)
    rect( 600, 400, 100, 100)
    image(dice, 600, 400, 100, 100, 100*RandomDice, 0, 100+100*RandomDice, 97)
    '''
    squareXShow = startSquareX
    Fill = startFill
    for i in range( numSquares ):
        fill ( Fill )
        rect( squareXShow, squareYShow, squareWidth, squareHeight )
        Fill = Fill + 20
        squareXShow = squareXShow + squareWidth        
    squareXShow = startSquareX    
    for i in range(numSquares):    
        if not(activeSquares[i]):
            fill (0)
            rect( squareXShow, squareYShow, squareWidth, squareHeight )
        squareXShow = squareXShow + squareWidth 

    print ( "X", mouseX )
    print ( "Y", mouseX )
    print ( activeSquares )
    delay ( 500 )
    '''
        
        
        
        
