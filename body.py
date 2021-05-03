import pygame
from Chess.constants import *
from pygame.rect import *
import math, asyncio
from pygame.sprite import Sprite

pygame.init()
g = pygame.sprite.Group()


class pawn(Sprite):
    def __init__(self, x, y, win, board, type):
        Sprite.__init__(self, g)
        self.x = x
        self.y = y
        self.move = False
        self.firstPos = True
        self.moves = self.getMoves(pawn, board)
        self.selected = False
        self.coor = (self.x, self.y)
        self.rect = pygame.Rect(x, y, x + 1, y + 1)
        self.moveable = False
        self.increment = 1
        self.type = type
        self.left, self.right = False, False
        if self.type == "White":

            self.image = Chess
            self.mask = pygame.mask.from_surface(self.image)
            display(self.image, self.x, self.y, win)
        elif self.type == "Black":
            self.image = Blue
            self.mask = pygame.mask.from_surface(self.image)
            display(self.image, self.x, self.y, win)

    def MakeCircle(self, win, object):
        win.blit(Blue, (int(change(object.x) + 10), int(change(object.y) + 10)))

    def moveLeft(self, board):
        if self.left and not self.right and self.selected:
            self.left, self.selected = False, False
            if self.type == "White":
                a = self.x
                b = self.y
                c = a - 1
                d = b - 1
                if board[d][c] == "0":
                    print("Left")
                    (board[b][a], board[d][c]) = (board[d][c], board[b][a])
                elif not board[d][c] == "0":
                    print(c, d)
                    (board[b][a], board[d - 1][c - 1]) = (board[d - 1][c - 1], board[b][a])
            elif self.type == "Black":
                a = self.x
                b = self.y
                c = a - 1
                d = b + 1
                if board[d][c] == "0":
                    (board[b][a], board[d][c]) = (board[d][c], board[b][a])

    def moveRight(self, board):
        if self.right and not self.left and self.selected:
            self.right, self.selected = False, False
            if self.type == "White":
                a = self.x
                b = self.y
                c = a + 1
                d = b - 1
                (board[b][a], board[d][c]) = (board[d][c], board[b][a])
                if board[d][c] == "0":
                    (board[b][a], board[d][c]) = (board[d][c], board[b][a])
                    print("Moved right")

            elif self.type == "Black":
                a = self.x
                b = self.y
                c = a + 1
                d = b + 1
                (board[b][a], board[d][c]) = (board[d][c], board[b][a])
                """if board[d][c] != '0':
                    (board[b][a], board[d][c]) = (board[d][c], board[b][a])
                    board[d][c] = '0'
                    (board[b][a], board[d][c]) = (board[d][c], board[b][a])"""

    def JumpRight(self, board):
        if self.type == "White":
            a = self.x
            b = self.y
            c = a + 2
            d = b - 2
            (board[b][a], board[d][c]) = (board[d][c], board[b][a])
        elif self.type == "Black":
            a = self.x
            b = self.y
            c = a + 2
            d = b + 2
            print(c, d)
            (board[b][a], board[d][c]) = (board[d][c], board[b][a])

    def JumpLeft(self, board):
        if self.type == "White":
            a = self.x
            b = self.y
            c = a - 2
            d = b - 2
            (board[b][a], board[d][c]) = (board[d][c], board[b][a])
        elif self.type == "Black":
            a = self.x
            b = self.y
            c = a - 2
            d = b + 2
            (board[b][a], board[d][c]) = (board[d][c], board[b][a])

    def draw(self, win):
        win.blit(self.image, self.coor)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def drawCircle(self, surface, x, y):
        x = int(x)
        y = int(y)
        print(x, y)
        drawRec(surface, x, y - 100, 50, 50)

    def MakeCircle(self, win, object):
        win.blit(Blue, (int(change(object.x) + 10), int(change(object.y) + 10)))

    def getMoves(self, type, board):
        if isinstance(type, pawn):
            return list((type.x, type.y - 1), (type.x, type.y - 2))

    @classmethod
    def adder(cls):
        g.add(cls)


class point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(pygame.sprite.Sprite, self).__init__()
        self.x = x
        self.y = y
        self.image = Circle
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(x, y, x + 1, y + 1)


class thing:
    def __init__(self, row, col):
        self.x = row
        self.y = col


class Game():
    def __init__(self, win):
        self.win = win
        self.turn = 1
        self.done = True
        self.board = [
            ['0', '2', '0', '2', '0', '2', '0', '2'],
            ['2', '0', '2', '0', '2', '0', '2', '0'],
            ['0', '2', '0', '2', '0', '2', '0', '2'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['1', '0', '1', '0', '1', '0', '1', '0'],
            ['0', '1', '0', '1', '0', '1', '0', '1'],
            ['1', '0', '1', '0', '1', '0', '1', '0']
        ]
        self.chosenpiece = None

    Pawns = set()
    Black = set()
    Pieces = []
    Blacks = []

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1

    def makeBoard(self):
        for i in range(8):
            for j in range(8):
                if odd(i) and even(j):
                    drawRec(self.win, i, j, 100, 100)
                if odd(i) and odd(j):
                    drawRec(self.win, i + 1, j, 100, 100)
                if even(i) and odd(j):
                    drawRec(self.win, i, j, 100, 100)

    def drawPawns(self):
        for x in ranleg(self.board):
            for y in ranleg(self.board[x]):
                if self.board[x][y] == '1':
                    self.p1 = pawn(y, x, self.win, self.board, "White")
                    self.Pawns.add(self.p1)
                elif self.board[x][y] == '2':
                    self.p2 = pawn(y, x, self.win, self.board, "Black")
                    self.Black.add(self.p2)

    def drawPieces(self):
        for x in ranleg(self.board):
            for y in ranleg(self.board[x]):
                if self.board[x][y] == '1':
                    self.p1 = pawn(y, x, self.win, self.board, "White")
                elif self.board[x][y] == '2':
                    self.p2 = pawn(y, x, self.win, self.board, "Black")

    def getSet(self):
        Pieces = list(self.Pawns)

        return Pieces

    def getBLACKSet(self):
        Pieces1 = list(self.Black)
        return Pieces1

    def iterate(self, thing, x, y):
        thing = list(thing)
        print(thing)
        for _ in ranleg(thing):
            if thing[_].x == x and thing[_].y == y:
                print("Iterated")

                thing[_].x = 2000
                thing.remove(thing[_])
                return True
        return False

    def check(self, row, col, type):
        x, y = MosInput()
        x, y = changer(x), changer(y)
        piece = thing(row, col)
        if piece is not None:
            if not isinstance(piece, pawn):
                if type == "White" and self.turn == 1 and self.done:
                    if Collides(piece.x + 1, piece.y - 1, MosInput()[0], MosInput()[1]) and self.board[piece.y - 1][
                        piece.x + 1] == '0' and self.turn == 1:
                        print("ok")
                        self.turn = 2
                        self.board[piece.y - 1][piece.x + 1], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y - 1][
                                                                                                 piece.x + 1]

                    if Collides(piece.x - 1, piece.y - 1, x, y) and self.board[piece.y - 1][
                        piece.x - 1] == '0' and self.turn == 1:
                        self.board[piece.y - 1][piece.x - 1], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x],self.board[piece.y - 1][piece.x - 1]
                    if Collides(piece.x - 2, piece.y - 2, x, y) and self.board[piece.y - 1][
                        piece.x - 1] != '0' and self.board[piece.y - 1][
                        piece.x - 1] != '1' and self.board[piece.y - 2][piece.x - 2] == "0" and self.turn == 1:
                        self.turn = 2
                        self.board[piece.y - 1][piece.x - 1] = "0"
                        self.board[piece.y - 2][piece.x - 2], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y - 2][
                                                                                                 piece.x - 2]


                    elif Collides(piece.x + 2, piece.y - 2, x, y) and self.board[piece.y - 1][
                        piece.x + 1] != '0' and self.board[piece.y - 1][
                        piece.x + 1] != '1' and self.board[piece.y - 2][piece.x + 2] == "0" and self.turn == 1:
                        self.turn = 2
                        self.board[piece.y - 1][piece.x + 1] = "0"
                        self.board[piece.y - 2][piece.x + 2], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y - 2][
                                                                                                 piece.x + 2]


                elif type == "Black" and self.turn == 2 and self.done:
                    if Collides(piece.x - 1, piece.y + 1, x, y) and self.board[piece.y + 1][
                        piece.x - 1] == '0' and self.turn == 2:
                        print(piece.x, piece.y)
                        self.turn = 1
                        self.board[piece.y + 1][piece.x - 1], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y + 1][
                                                                                                 piece.x - 1]
                    elif Collides(piece.x - 2, piece.y + 2, x, y) and self.board[piece.y + 1][
                        piece.x - 1] != '0' and self.board[piece.y + 1][
                        piece.x - 1] != '2' and self.board[piece.y + 2][
                        piece.x - 2] == "0" and self.turn == 2:
                        self.turn = 1
                        self.board[piece.y + 1][piece.x - 1] = "0"
                        self.board[piece.y + 2][piece.x - 2], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y + 2][
                                                                                                 piece.x - 2]
                    if Collides(piece.x + 1, piece.y + 1, x, y) and self.board[piece.y + 1][
                        piece.x + 1] == '0' and self.turn == 2:
                        self.turn = 1
                        self.board[piece.y + 1][piece.x + 1], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y + 1][
                                                                                                 piece.x + 1]

                    elif Collides(piece.x + 2, piece.y + 2, x, y) and self.board[piece.y + 1][
                        piece.x + 1] != '0' and self.board[piece.y + 1][
                        piece.x + 1] != '2' and self.board[piece.y + 2][piece.x + 2] == "0" and self.turn == 2:
                        self.turn = 1
                        self.board[piece.y + 1][piece.x + 1] = "0"
                        self.board[piece.y + 2][piece.x + 2], self.board[piece.y][piece.x] = self.board[piece.y][
                                                                                                 piece.x], \
                                                                                             self.board[
                                                                                                 piece.y + 2][
                                                                                                 piece.x + 2]
                    self.done = False



# Lamb functions
changes = lambda Value: (Value + 0.2) * 100
change = lambda Value: Value * 100
ranleg = lambda Value: range(len(Value))
changer = lambda Value: Value // 100
even = lambda Value: True if Value % 2 == 0 else False
odd = lambda Value: True if Value % 2 == 1 else False
drawRec = lambda win, x, y, sizeX, sizeY: pygame.draw.rect(win, Black, (change(x), change(y), sizeX, sizeY))
display = lambda image, x, y, win: win.blit(image, (changes(x), changes(y)))
test = lambda Value: True if Value < 27 else False


# Normal Functions
def isCollision(enemyX, enemyY, bulletX, bulletY) -> int:
    distance = int(math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))))

    if distance < 27:
        return True
    else:
        return False


def Collides(enemyX, enemyY, bulletX, bulletY) -> int:
    enemyX *= 100
    enemyY *= 100
    bulletX *= 100
    bulletY *= 100
    distance = int(math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))))
    if distance < 1:
        return True
    else:
        return False


def MosInput():
    x, y = pygame.mouse.get_pos()
    return x // 100, y // 100
