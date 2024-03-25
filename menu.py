import time

import pygame
from button import Button


class Menu():
    def __init__(self, screenSize):
        pygame.init()

        self.screenSize = screenSize[0], screenSize[1]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.backgroundImg = pygame.image.load("images/empty-block.png")
        self.backgroundImg = pygame.transform.scale(self.backgroundImg, (50, 50))

        self.size = None
        self.prob = None
        self.returnScreenSize = None
        self.time = None

        self.difficulty = None
        self.game_time = None
        game_mode = Button((200, 150), "Game difficuty")
        dif_easy = Button((200, 300), "Easy", 1)
        dif_mediu = Button((200, 450), "Medium", 2)
        dif_hard = Button((200, 600), "Hard", 3)
        game_time = Button((200, 150), "Game duration")
        time_short = Button((200, 300), "150SEC", 1)
        time_medium = Button((200, 450), "300SEC", 2)
        time_long = Button((200, 600), "600SEC", 3)
        self.buttons = [game_mode, dif_easy, dif_mediu, dif_hard, game_time, time_short, time_medium, time_long]

    def run(self):
        running = True

        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.difficulty is None:
                        for i in range(1, 4):
                            if self.buttons[i].checkForInput(mouse_pos):
                                self.difficulty = self.buttons[i].returnValue()
                                self.setDifficulty()

                    elif self.difficulty is not None:
                        for i in range(5, 8):
                            if self.buttons[i].checkForInput(mouse_pos):
                                self.game_time = self.buttons[i].returnValue()
                                self.setTime()

            if self.difficulty is None:
                for i in range(0, 4):
                    self.buttons[i].update(self.screen)
            if self.difficulty is not None and self.game_time is None:
                for i in range(4, 8):
                    self.buttons[i].update(self.screen)

            if self.difficulty is not None and self.game_time is not None:
                running = False
                return self.size, self.prob, self.returnScreenSize, self.time

            pygame.display.flip()
            self.update()

        pygame.quit()

    def update(self):
        width, height = 0, 0
        while height < self.screenSize[1]:
            while width < self.screenSize[0]:
                self.screen.blit(self.backgroundImg, (width, height))
                width += self.backgroundImg.get_width()
            width = 0
            height += self.backgroundImg.get_height()

    def setDifficulty(self):
        if self.difficulty == 1:
            self.size = (15, 10)
            self.prob = 0.05
            self.returnScreenSize = 400, 800

        elif self.difficulty == 2:
            self.size = (15, 15)
            self.prob = 0.14
            self.returnScreenSize = 600, 800

        elif self.difficulty == 3:
            self.size = (15, 20)
            self.prob = 0.18
            self.returnScreenSize = 800, 800

    def setTime(self):
        if self.game_time == 1:
            self.time = 150

        elif self.game_time == 2:
            self.time = 300

        elif self.game_time == 3 :
            self.time = 600

    def menuExit(self):
        print(self.size)
        print(self.prob)
        print(self.returnScreenSize)
        print(self.time)
        return self.size, self.prob, self.returnScreenSize, self.time










