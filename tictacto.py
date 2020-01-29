matrix = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def rematch1():
    regam = input("Would you like to play again? type Y/N")
    if regam == ("y" or "Y"):
        matrix = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
        startGame1()
    else:
        print('Goodbye')

def endGame1():
    if (matrix['one']==matrix['two']==matrix['three'] or matrix['four']==matrix['five']==matrix['six'] or matrix['seven']==
    matrix['eight']==matrix['nine']) and (matrix['one'] or matrix['five'] or matrix['seven'])==('X' or 'O'):
        return True
    
    elif (matrix['one']==matrix['four']==matrix['seven'] or matrix['two']==matrix['five']==matrix['eight'] or matrix['three']==
          matrix['six']==matrix['nine']) and (matrix['one'] or matrix['two'] or matrix['three'])==('X' or 'O'):
        return True
    
    elif (matrix['one']==matrix['five']==matrix['nine'] or matrix['three']==matrix['five']==
          matrix['seven']) and (matrix['one'] or matrix['three'])==('X' or 'O') :
        return True
    
    elif (matrix['one'] and matrix['two'] and matrix['three'] and matrix['four'] and matrix['five'] and 
          matrix['six'] and matrix['seven'] and matrix['eight'] and matrix['nine']) == ('X' or 'O'):
        return 'Tie'
    else:
        return False
        
def midGame1():
    global matrix
    while endGame1() == False:
        p1p = str(input("Choose where you want to place X by selecting a number: ")) 
        for x,y in matrix.items():
            if y == p1p:
                matrix[x] = 'X'
    
        p2p = str(input("Choose where you want to place O by selecting a number: "))
        for x,y in matrix.items():
            if y == p2p:
                matrix[x] = 'O'
        board1()
        
    else:
        if endGame1() == True:
            print("We have a winner!!!")
            rematch1()
        
        elif endGame1() == 'Tie':
            print("It is a tie!!")
            rematch1()


def board1(): 
    print(f"{matrix['one']}|{matrix['two']}|{matrix['three']}")
    print("-----")
    print(f"{matrix['four']}|{matrix['five']}|{matrix['six']}")
    print("-----")
    print(f"{matrix['seven']}|{matrix['eight']}|{matrix['nine']}")

def startGame1():
    start = str(input("Shall we start?(enter Y/N)"))
    if start == ("Y" and "y"):
        board1()
        midGame1()
        
    else:
        print("Good Bye...") 

if __name__ == "__main__":
    startGame1()