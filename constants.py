import pygame, os

White = (255, 255, 255)
size = (800, 800)
Black = (0, 0, 0)
Pos = False
Chess = pygame.transform.scale(pygame.image.load(os.path.join("images", "CHECKER.png")), (64, 64))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("images", 'record (1).png')), (20, 20))
yellow = (0, 255, 255)
Blue = pygame.transform.scale(pygame.image.load(os.path.join("images", 'BLUE.png')), (64, 64))
