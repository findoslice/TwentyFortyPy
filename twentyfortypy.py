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
            while True:
                newNode = self.board[self.random.randint(0,15)]
                if newNode[1] == None:
                    newVal = self.random.choice([2,2,4])
                    for j in range(len(self.board)):
                        if self.board[j][0] == newNode[0]:
                            print (newNode[0])
                            self.board = self.board[:j] + [(self.board[j][0], newVal)] + (self.board[j+1:] or [])
                    break
                else:
                    pass
    
    def currentState(self):
        return self.board
