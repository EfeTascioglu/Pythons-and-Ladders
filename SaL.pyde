

def setup():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global backdrop
    allBoundaries = []
    startSquareX = 100
    startSquareY = 200
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 200
    squareWidth = 200
    numSquares = 5
    removeSquare = True
    startFill = 20
    whichSquare = -1
    banner = loadImage("banner.png")
    backdrop = loadImage("snakes.png")
    dice = loadImage("dice.png")
    size ( 1000, 700 )
    
    for i in range( numSquares ):
        upperLeft =  [ squareXShow, squareYShow ]
        lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        squareXShow = squareXShow + squareWidth
    
    activeSquares = [ True for i in range( numSquares ) ]

#    activeSquares[ 4 ] = False                  These just show what happened
#    print ( activeSquares )
            
#    print ( allboundaries )
#    print ( allboundaries[ 1 ])
#    print ( allboundaries[ 1 ][1])
#    print ( allboundaries[ 1 ][1][0] )
    
    
        
    
    
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares
    
#  all Boundaries is a list of tuples,  each tuple is the upper left and lower right of each box
#  if removeSquare is True, you will not be able to click again in that square again as that place in activeSquares will be turned to False
    whichSquare = - 1
    keepGoing = False
    for i in range( numSquares ):
        if activeSquares[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                keepGoing = True
                break
    if keepGoing:
        if validLocation and removeSquare:
            activeSquares[ whichSquare ] = False
    print ( whichSquare )
        
        
    

def draw():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global backdrop
   
    image(backdrop, 0, 0, 800, 700)
    image(banner, 800, 
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
        
        
        
        
