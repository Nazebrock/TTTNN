from tictactoe import Tictactoe, IA

def get_possibilities():

    t = Tictactoe()
    res = []

    def convertPos( x):
        if x < 3:
            return [0,x]
        else:
            return [(x//3), (x%3)]

    def possibilities( game):
        if game.testWin() == 0:
            for move in game.getMoves():
                possibilities(game.getNewState(convertPos(move)))
            res.append(game.export())
        return

    possibilities(t)
    return res

def generate_data():

    possibilities = get_possibilities()
    train = open("NeuralNetwork/train.data", "w")
    test = open("NeuralNetwork/test.data", "w")

    train.write(str(len(possibilities)/2)+" 9 1\n")

    def nnWrite(file, board, sol):
        file.write(board+"\n"+str(sol)+"\n")

    def getBoardAsString(possibilitie):
        res = ""
        for tab in possibilitie[0]:
            for i in tab:
                res = res + str(i) + " "
        return res

    for i in range(len(possibilities)):
        possibilitie = possibilities[i]
        t = Tictactoe(data=possibilitie)
        ia = IA(t, (t.turn%2)+1)
        ia.minimax(ia.game, 0)
        res = ia.choice

        if i < len(possibilities)/2:
            nnWrite(train, getBoardAsString(possibilitie), res)
        else:
            nnWrite(test, getBoardAsString(possibilitie), res)

"""generate_data()"""

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

p = get_possibilities()
print(len(p))
print(len(f7(p)))
