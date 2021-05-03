import asyncio, pygame, os, sys
from Chess.constants import *
from Chess.body import *
import pyglet

pygame.init()

win = pygame.display.set_mode(size)

global MouseClicked
game = Game(win)

game.drawPawns()


async def main():
    gameover = False
    while not gameover:
        await asyncio.gather(
            redraw()

        )


async def redraw():
    win.fill(White)
    game.makeBoard()
    game.drawPieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.Pieces = game.getSet()
            game.Blacks = game.getBLACKSet()
            x, y = pygame.mouse.get_pos()
            x = change(changer((x)))
            y = change(changer((y)))
            for i in ranleg(game.board):
                for j in ranleg(game.board[i]):
                    if MosInput()[0] == i and MosInput()[1] == j and game.turn == 1:
                        print("ok")
                        game.check(game.Pieces[i].x, game.Pieces[i].y, "White")
            for i in ranleg(game.board):
                for j in ranleg(game.board[i]):
                    if MosInput()[0] == i and MosInput()[1] == j and game.turn == 2:
                        game.check(game.Blacks[i].x, game.Blacks[i].y, "Black")

    pygame.display.flip()

    pygame.display.update()


asyncio.run(main())
