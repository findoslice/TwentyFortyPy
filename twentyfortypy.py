class TwentyFortyPy:
    import random

    def __init__(self):
        self.GenerateBoard()


    def GenerateBoard(self):
        self.board = [((0,0), None), ((0,1), None), ((0,2), None), ((0,3), None),
                      ((1,0), None), ((1,1), None), ((1,2), None), ((1,3), None),
                      ((2,0), None), ((2,1), None), ((2,2), None), ((2,3), None),
                      ((3,0), None), ((3,1), None), ((3,2), None), ((3,3), None)
                     ]
        for i in range(2):
            self.AddRandValue()
        return self.board
    
    def CurrentState(self):
        return self.board
    
    def ChangeValue(self, coords, newvalue):
        coords = coords
        newvalue = newvalue
        for j in range(len(self.board)):
            if self.board[j][0] == coords:
                self.board = self.board[:j] + [(coords, newvalue)] + (self.board[j+1:] or [])

    def AddRandValue(self):
        while True:
                newNode = self.board[self.random.randint(0,15)]
                if newNode[1] == None:
                    newVal = self.random.choice([2,2,4])
                    self.ChangeValue(newNode[0], newVal)
                    break
                else:
                	pass
				

    def ShiftUp(self):
        y = str(board)
        for x in self.board:
            if x[1] is not None:
                for i in range(1,4):
                    
                    if ((x[0][0]-i, x[0][1]), x[1]) in self.board:
                        self.ChangeValue((x[0][0] - i, x[0][1]), x[1]*2)
                        self.ChangeValue((x[0][0] - i + 1, x[0][1]), None)
                        break

                    if ((x[0][0]-i, x[0][1]), None) in self.board:
                        self.ChangeValue((x[0][0] - i, x[0][1]), x[1])
                        self.ChangeValue((x[0][0] - i + 1, x[0][1]), None)
					
        if y != str(self.board):
            self.AddRandValue()
            return True
        else:
            return False
        

    def Prettify(self):
        x = self.board
        y = []
        for elem in x:
            y.append(elem[1])
        while y != []:
            print (y[:4])
            y = y[4:]

if __name__ == "__main__":
    board = TwentyFortyPy()
    board.Prettify()
    print ("\n")
    for i in range(20):
        board.ShiftUp()
        board.Prettify()
        print("\n")