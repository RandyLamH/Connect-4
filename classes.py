import pygame
import os
import random
from pygame.sprite import Sprite, Group

images = os.listdir("images")

UPDATE_SURFACE = []
INV_CLASS = []
INV_SURFACE = []
SLIDE = []

class Piece(Sprite):
    def __init__(self, color = "red"):
        super().__init__()
        self.piece = pygame.Surface((86,86))
        self.piece.fill((255, 255, 255))
        self.circle = None
        self.modified = False
        self.color = None
        self.x = 0
        self.y = 100
        self.max_y = 0

    def update_image(self, turn, x, y, color1 = (255, 0, 0), color2 = (255,255,0)):
        self.x = x
        self.max_y = y
        if turn == 1:
            self.circle = pygame.draw.circle(self.piece, color1, (43,43), 43)
            self.color = color1
        if turn == 2:
            self.circle = pygame.draw.circle(self.piece, color2, (43, 43), 43)
            self.color = color2
        self.modified = True


    def shown(self):
        self.piece = pygame.image.load("images/red_piece.jpg")
        self.piece = pygame.transform.scale(self.piece, (86, 86))

    def update_shown(self, turn, color1 = "images/red_piece.jpg", color2 = "images/yellow_piece.jpg"):
        if turn == 1:
            self.piece = pygame.image.load(color1)
            self.piece = pygame.transform.scale(self.piece, (86, 86))
        if turn == 2:
            self.piece = pygame.image.load(color2)
            self.piece = pygame.transform.scale(self.piece, (86, 86))
        self.modified = True

    def reset(self):
        self.__init__()
class InvRect: #Invinsible Rectangle
    def __init__(self):
        self.surface = pygame.Surface((86,822))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()
        pygame.draw.rect(self.surface, (255, 255, 255, 0), self.rect)
class GameBoard:
    def __init__(self,rows,column):
        self.board = pygame.image.load("images/game_board.png")
        for x in range(rows):
            for y in range(column):
                piece = Piece()
                UPDATE_SURFACE.append((piece,(13 + x * 100, 212 + y * 100)))
        UPDATE_SURFACE.reverse()

        for x in range(rows):
            rect = InvRect()
            INV_CLASS.append((rect, ((13 + x * 100, 0))))
            INV_SURFACE.append((rect.surface, ((13 + x * 100, 0))))

class Button():
    def __init__(self,  text, x , y):
        self.text = text
        self.x = x

        self.y = y
        self.rect = pygame.rect.Rect((self.x, self.y), (200, 50))
    def draw(self, window):

        pygame.draw.rect(window, (255, 255, 255), self.rect, 0 , 7)
        if self.button_click():
            pygame.draw.rect(window, (200, 200, 200), self.rect, 0, 7)
            return True
        else:
            pygame.draw.rect(window, (255, 255, 255), self.rect, 0, 7)


    def button_click(self):
        left_click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        if left_click and self.rect.collidepoint(mouse_pos):
            return True
        else: return False
    def play(self, window):
        if self.draw(window):

            if pygame.mouse.get_pressed()[0] == True:

                return False


        return True

    def draw_text(self, window, font, text_col, x, y):
        img = font.render(self.text, True, text_col)
        window.blit(img, (x, y))


class MainMenu():
    def __init__(self, toggle_button, settings_button, play_button):
        self.toggle_button = toggle_button
        self.play = play_button
        self.settings = settings_button
        self.back_arrowrect = Button(None, 0, 75)
        self.show_settings = False
    def settings_scene(self):
        posit = pygame.mouse.get_pos()

        if self.settings.rect.collidepoint(posit) and pygame.mouse.get_pressed()[0]:
            self.show_settings = True

    def back_scene(self):
        posit = pygame.mouse.get_pos()
        if self.back_arrowrect.rect.collidepoint(posit) and pygame.mouse.get_pressed()[0]:
            self.show_settings = False

