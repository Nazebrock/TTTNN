from copy import deepcopy

""" Class for Human player """
class Player:

    def __init__(self):
        return

    def getPos(self):
        coordinate = raw_input("Enter coordinate (x y): ")
        coordinate = coordinate.split(' ', 1)
        while len(coordinate) != 2 :
            print("Wrong coordinate format (x y): ")
            coordinate = input()
            coordinate = coordinate.split(' ')
        return [int(c) for c in coordinate]

""" Class for MiniMax IA """
class IA:

    def __init__(self, game, number):
        self.game = game
        self.choice = 0
        self.me = number
        if number == 1:
            self.opponent = 2
        else:
            self.opponent = 1
        
    def convertPos(self, x):
        if x < 3:
            return [0,x]
        else:
            return [(x//3), (x%3)]

    def score(self, game, depth):
        if game.testWin() == self.me:
            return 10 - depth
        elif game.testWin() == self.opponent:
            return depth - 10
        else:
            return 0 

    def minimax(self, game, depth):
        if game.testWin() != 0 or depth == 9 - game.turn:
            return self.score(game, depth)

        depth += 1
        scores = []
        moves = []
        for move in game.getMoves():
            possible_game = game.getNewState(self.convertPos(move))
            scores.append(self.minimax(possible_game, depth))
            moves.append(move)
        
        if (game.turn%2)+1 == self.me:
            max_index = scores.index(max(scores))
            self.choice = moves[max_index]
            return scores[max_index]
        else:
            min_index = scores.index(min(scores))
            self.choice = moves[min_index]
            return scores[min_index]

    def getPos(self):
        self.minimax(self.game, 0)
        return self.convertPos(self.choice)

""" Class Manager for the game """
class Tictactoe:

    def __init__(self, data=[[[0,0,0] for i in range(3)], 0]):
        self.board = data[0]
        self.winner = 0
        self.turn = data[1]

    """ Export datas of the game in the format [turn, board]"""
    def export(self):
        return [self.board, self.turn]

    """ Return a new instance of Tictactoe after playing a move"""
    def getNewState(self, pos):
        t = deepcopy(self) 
        t.play((self.turn%2)+1, pos)
        t.turn += 1
        return t

    """ Return a list of the possible moves """
    def getMoves(self):
        res = []
        for i in range (len(self.board)):
            for j in range (len(self.board[0])):
                if self.board[i][j] == 0:
                    res.append((i*3)+j)
        return res

    """ Test the move and record it if it is legit 
        Return -1 if it is illegal 0 if it is not """
    def play(self, player, pos):
        if pos[0] < 0 or pos[0] > 2 or pos[1] < 0 or pos[1] > 2:
            print("out")
            return -1

        if self.board[pos[0]][pos[1]] != 0 :
            print("taken")
            return -1
        
        self.board[pos[0]][pos[1]] = player
        return 0

    """ Draw the board """
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

    """ Test if there is a winner
        Return the number of the player if he won and 0 if there is no winner"""
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
    
    """ Run the game """
    def run(self, players=[Player(), Player()]):

        while(self.winner == 0 and self.turn < 9):
            print("Player "+str((self.turn%2)+1)+" turn")
            self.draw()
            coordinate = players[self.turn%2].getPos()
            while(self.play((self.turn%2)+1, coordinate) == -1):
                print("Wrong coordinate : "+str(coordinate))
                coordinate = players[self.turn%2].getPos()
            self.turn += 1
            self.winner = self.testWin()

        if self.winner != 0:
            print("Player "+str(self.winner)+" win !")
            self.draw()
        else:
            print("Draw")
            self.draw()

