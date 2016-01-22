import pygame, sys
from pygame.locals import *
import threading


class IntrusionAlarm(object):
    # set up the colors
    BLACK = (40, 104, 20)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (30, 255, 77)
    BLUE = (71, 109, 255)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # set up the window
        self.windowSurface = pygame.display.set_mode((500, 400), 0, 32)
        pygame.display.set_caption('Warning!!!')
        # set up fonts
        basicFont = pygame.font.SysFont(None, 48)

        # set up the text
        self.text = basicFont.render('Intruder Alert !!!', True, self.GREEN, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.windowSurface.get_rect().centerx
        self.textRect.centery = self.windowSurface.get_rect().centery

        # draw the white background onto the surface
        self.windowSurface.fill(self.BLUE)


        # set up alarm sound
        pygame.mixer.music.load("resources/siren.mp3")

    def run(self):
        # draw the text's background rectangle onto the surface
        pygame.draw.rect(self.windowSurface, self.RED, (
            self.textRect.left - 20, self.textRect.top - 20, self.textRect.width + 40, self.textRect.height + 40))

        # get a pixel array of the surface
        pixArray = pygame.PixelArray(self.windowSurface)
        pixArray[480][380] = self.BLACK
        del pixArray

        # draw the text onto the surface

        self.windowSurface.blit(self.text, self.textRect)
        pygame.mixer.music.play(-1)

        # draw the window onto the screen
        pygame.display.update()
