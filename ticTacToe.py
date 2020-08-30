theBoard={'top-L':'  ','top-M':'  ','top-R':'  ','mid-L':'  ','mid-M':'  ','mid-R':'  ','low-L':'  '
,'low-M':'  ','low-R':'  '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('--+--+--')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#printBoard(theBoard)

turn='X'
for i in range(0,9):
    printBoard(theBoard)
    print("Its your turn "+ turn + ". Enter the location you want to mark. " )
    location=input()
    theBoard[location]=turn+' '
    if turn=='X':
        turn='O'
    else:
        turn='X'