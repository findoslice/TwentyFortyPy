class TwentyFortyPy:
    import random

    def __init__(self):
        self.generateBoard()


    def generateBoard(self):
        self.board = [((0,0), None), ((0,1), None), ((0,2), None), ((0,3), None),
                      ((1,0), None), ((1,1), None), ((1,2), None), ((1,3), None),
                      ((2,0), None), ((2,1), None), ((2,2), None), ((2,3), None),
                      ((3,0), None), ((3,1), None), ((3,2), None), ((3,3), None)
                     ]
        for i in range(2):
            self.addRandValue()
    
    def currentState(self):
        return self.board
    
    def changeValue(self, coords, newvalue):
        coords = coords
        newvalue = newvalue
        for j in range(len(self.board)):
                        if self.board[j][0] == coords:
                            self.board = self.board[:j] + [(coords, newvalue)] + (self.board[j+1:] or [])

    def addRandValue(self):
        while True:
                newNode = self.board[self.random.randint(0,15)]
                if newNode[1] == None:
                    newVal = self.random.choice([2,2,2,2,4])
                    self.changeValue(newNode[0], newVal)
                    break
                else:
                    pass

if __name__ == "__main__":
    board = TwentyFortyPy()
    print (board.currentState())
    print ("\n\n")
    board.changeValue((0,0), 16)
    print (board.currentState())