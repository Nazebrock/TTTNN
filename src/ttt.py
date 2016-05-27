class Tictactoe:
    board = [[0,0,0] for i in range(3)]

    def __init__(self):
        return

    def play(self, player, pos):

        if self.board[pos[0]][pos[1]] != 0:
            return -1
        
        self.board[pos[0]][pos[1]] = player
        return 0

    def draw(self):
        print("-------")
        for i in range (len(self.board)):
            row = "|"
            for j in range (len(self.board[0])):
                c = " |"
                if self.board[i][j] == 1:
                    c = "x|"
                elif self.board[i][j] == 2:
                    c = "o|"
                row = row + c
            print(row)
            print("-------")

    def testWin(self):
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            elif self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[2][0] != 0 and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
        else:
            return 0
    
t = Tictactoe()
winner = 0
turn = 0

def getPos():
    print("Enter coordinate (x y): ")
    coordinate = input()
    coordinate = coordinate.split(' ', 1)
    while(len(coordinate) != 2):
        print("Wrong coordinate format (x y): ")
        coordinate = input()
        coordinate = coordinate.split(' ')
    return [int(c) for c in coordinate]

while(winner == 0 and turn < 9):
    print("Player "+str((turn%2)+1)+" turn")
    t.draw()
    coordinate = getPos()
    t.play((turn%2)+1, coordinate)
    turn += 1
    winner = t.testWin()

if winner != 0:
    print("Player "+str(winner)+" win !")
    t.draw()
else:
    print("Draw")
    t.draw()
