class Board(object):
    def __init__(self, boardString):
        self.board = []
        self.boardString = boardString

        self.horizontals = []
        self.verticals = []
        self.blocks = []
        for x in range(9):
            self.horizontals.append([])
            self.verticals.append([])
            self.blocks.append([])

        if len(boardString) == 81:
            counter = 0
            for i in range(9):
                self.board.append([])
                for j in range(9):
                    self.board[i].append(boardString[counter])
                    if i % 9 in [0, 1, 2] and j % 9 in [0, 1, 2]:
                        self.blocks[0].append(boardString[counter])
                    elif i % 9 in [0, 1, 2] and j % 9 in [3, 4, 5]:
                        self.blocks[1].append(boardString[counter])
                    elif i % 9 in [0, 1, 2] and j % 9 in [6, 7, 8]:
                        self.blocks[2].append(boardString[counter])
                    elif i % 9 in [3, 4, 5] and j % 9 in [0, 1, 2]:
                        self.blocks[3].append(boardString[counter])
                    elif i % 9 in [3, 4, 5] and j % 9 in [3, 4, 5]:
                        self.blocks[4].append(boardString[counter])
                    elif i % 9 in [3, 4, 5] and j % 9 in [6, 7, 8]:
                        self.blocks[5].append(boardString[counter])
                    elif i % 9 in [6, 7, 8] and j % 9 in [0, 1, 2]:
                        self.blocks[6].append(boardString[counter])
                    elif i % 9 in [6, 7, 8] and j % 9 in [3, 4, 5]:
                        self.blocks[7].append(boardString[counter])
                    elif i % 9 in [6, 7, 8] and j % 9 in [6, 7, 8]:
                        self.blocks[8].append(boardString[counter])
                    counter += 1

        i = 0
        j = 9
        number = 0
        for x in range(9):
            for a in range(number + i, number + j):
                self.horizontals[x].append(boardString[a])
            i += 8
            j += 8
            number += 1

        for i in range(0, 81, 9):
            self.verticals[0].append(self.boardString[i])
            self.verticals[1].append(self.boardString[i + 1])
            self.verticals[2].append(self.boardString[i + 2])
            self.verticals[3].append(self.boardString[i + 3])
            self.verticals[4].append(self.boardString[i + 4])
            self.verticals[5].append(self.boardString[i + 5])
            self.verticals[6].append(self.boardString[i + 6])
            self.verticals[7].append(self.boardString[i + 7])
            self.verticals[8].append(self.boardString[i + 8])


    def getBlockID(self, r, c):
        if r in [0, 1, 2] and c in [0, 1, 2]:
            return 0
        elif r in [0, 1, 2] and c in [3, 4, 5]:
            return 1
        elif r in [0, 1, 2] and c in [6, 7, 8]:
            return 2
        elif r in [3, 4, 5] and c in [0, 1, 2]:
            return 3
        elif r in [3, 4, 5] and c in [3, 4, 5]:
            return 4
        elif r in [3, 4, 5] and c in [6, 7, 8]:
            return 5
        elif r in [6, 7, 8] and c in [0, 1, 2]:
            return 6
        elif r in [6, 7, 8] and c in [3, 4, 5]:
            return 7
        elif r in [6, 7, 8] and c in [6, 7, 8]:
            return 8

    def toString(self):
        line = ""
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                line += "+-----+-----+-----+\n"
            for j in range(9):
                if j == 0 or j == 3 or j == 6:
                    line += "|"
                if j in [0, 1, 3, 4, 6, 7]:
                    line += self.board[i][j] + " "
                else:
                    line += self.board[i][j]
            line += "|"
            if i != 8:
                line += "\n"
        line += "\n+-----+-----+-----+"

        return line


def cruncher(board):
    count = 0
    while not finished(board):
        for x in range(1, 10, 1):
            x = str(x)

            for blockID in range(9):
                block = board.blocks[blockID]
                posibilites = []
                block6 = []
                r, c = getBlockRowCol(blockID)
                # if blockID == 6:
                # print "Horizontals", board.horizontals[r]
                # print "Verticals",board.verticals[c]
                # print "debug"
                for i in range(9):
                    if block[i] == ".":
                        if x not in board.horizontals[r] and x not in board.verticals[c] \
                                and x not in board.blocks[blockID]:
                            posibilites.append(i)
                            posibilites.append(r)
                            posibilites.append(c)

                    if i % 3 == 2:
                        r += 1
                        c -= 3
                    c += 1

                if len(posibilites) == 3:
                    r = posibilites[1]
                    c = posibilites[2]
                    board.board[r][c] = x
                    board.horizontals[r][c] = x
                    board.verticals[c][r] = x
                    board.blocks[blockID][getBlockPosition(r, c)] = x
                    #print board.toString()
                    #print "here", x, r, c

            for r in range(9):
                for c in range(9):
                    cell = board.board[r][c]
                    blockID = board.getBlockID(r, c)
                    if cell == ".":
                        if r % 3 == 0:
                            r1 = r + 1
                            r2 = r + 2
                        elif r % 3 == 1:
                            r1 = r - 1
                            r2 = r + 1
                        else:
                            r1 = r - 2
                            r2 = r - 1
                        if c % 3 == 0:
                            c1 = c + 1
                            c2 = c + 2
                        elif c % 3 == 1:
                            c1 = c - 1
                            c2 = c + 1
                        else:
                            c1 = c - 2
                            c2 = c - 1
                        if x not in board.blocks[blockID] \
                                and ((x not in board.horizontals[r]
                                      and x in board.horizontals[r1]
                                      and x in board.horizontals[r2]
                                      and x not in board.verticals[c]
                                      and (board.board[c1] != "." and board.board[c2] != "."))
                                     or (x not in board.verticals[c]
                                         and x in board.verticals[c1]
                                         and x in board.verticals[c2]
                                         and x not in board.horizontals[r]
                                         and (board.board[r1] != "." and board.board[r2] != "."))):
                            board.board[r][c] = x  # + "<"
                            board.horizontals[r][c] = x
                            board.verticals[c][r] = x
                            board.blocks[blockID][getBlockPosition(r, c)] = x
                            # print board.toString()
                            #print

        count += 1

        if count > 500:
            break

            # for block in board.blocks:
            # print block


def getBoardPosition(blockPos, blockID):
    if blockID == 0 and blockPos == 0:
        return 0, 0


def getBlockRowCol(blockId):
    if blockId == 0:
        return 0, 0
    elif blockId == 1:
        return 0, 3
    elif blockId == 2:
        return 0, 6
    elif blockId == 3:
        return 3, 0
    elif blockId == 4:
        return 3, 3
    elif blockId == 5:
        return 3, 6
    elif blockId == 6:
        return 6, 0
    elif blockId == 7:
        return 6, 3
    elif blockId == 8:
        return 6, 6


def getBlockPosition(r, c):
    if r % 3 == 0 and c % 3 == 0:
        return 0
    elif r % 3 == 0 and c % 3 == 1:
        return 1
    elif r % 3 == 0 and c % 3 == 2:
        return 2
    elif r % 3 == 1 and c % 3 == 0:
        return 3
    elif r % 3 == 1 and c % 3 == 1:
        return 4
    elif r % 3 == 1 and c % 3 == 2:
        return 5
    elif r % 3 == 2 and c % 3 == 0:
        return 6
    elif r % 3 == 2 and c % 3 == 1:
        return 7
    elif r % 3 == 2 and c % 3 == 2:
        return 8


def finished(board):
    blocks = board.blocks
    horizontals = board.horizontals
    verticals = board.verticals
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(9):
        block = list(blocks[x])
        horiz = list(horizontals[x])
        verti = list(verticals[x])

        if block.sort() != numbers:
            return False
        if horiz.sort() != numbers:
            return False
        if verti.sort() != numbers:
            return False
    print "Finished"
    return True


def char_replacer(text):
    length = len(text)
    newtext = ""
    for i in range(length):
        if text[i] == "0":
            newtext += "."
        else:
            newtext += text[i]
    return newtext


print char_replacer("")
boardString = "5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3"
easy = "000079065000003002005060093340050106000000000608020059950010600700600000820390000"
easyDot = char_replacer(easy)

print easy
print easyDot

solved = "183279465469583712275461893342958176597136284618724359954812637731645928826397541"

board = Board(easyDot)

print board.toString()

cruncher(board)

print board.toString()

board = Board(solved)
cruncher(board)

print board.toString()