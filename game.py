import time
import pygame
import os


class Game():
    def __init__(self, board, screenSize, timp):
        pygame.init()
        self.board = board
        self.screenSize = screenSize[0], screenSize[1] - 100
        self.gameScreen = screenSize
        self.screen = pygame.display.set_mode(self.gameScreen)
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()
        self.startTime = time.time()
        self.endTime = timp

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                time.sleep(3)
                running = False
        pygame.quit()

    def draw(self):
        topLeft = (0, 100)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]
        self.drawTop()

    def drawTop(self):
        # desenez imaginea de sus
        img = pygame.image.load("images/0.png")
        scale = self.gameScreen[0] , 100
        img = pygame.transform.scale(img, scale)
        self.screen.blit(img, (0, 0))

        # desenez imaginea cu bomba si caut numarul de bombe si le desenez si pe ele
        img = pygame.image.load("images/unclicked-bomb.png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (25, 35))
        img = pygame.image.load("images/" + str(self.board.getNumBombs() // 10)
                                + str(self.board.getNumBombs() // 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (55, 35))
        img = pygame.image.load("images/" + str(self.board.getNumBombs() % 10)
                                + str(self.board.getNumBombs() % 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (85, 35))

        # desenez imaginea cu flagul, caut numarul de flaguri folosite si le desenez
        middle = self.gameScreen[0] // 2 - 45
        img = pygame.image.load("images/flag.png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (middle, 35))
        middle += 30
        img = pygame.image.load("images/" + str(self.board.getNumFlags() // 10)
                                + str(self.board.getNumFlags() // 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (middle, 35))
        middle += 30
        img = pygame.image.load("images/" + str(self.board.getNumFlags() % 10)
                                + str(self.board.getNumFlags() % 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (middle, 35))

        # scriu pe ecran timpul ramas pana se termina jocul
        timp = self.endTime - int((time.time() - self.startTime) // 1)
        if ((time.time() - self.startTime) // 1) > self.endTime or self.board.getLost():
            self.board.setLost()
            timp = 0
        img = pygame.image.load("images/" + str(timp // 100) + str(timp // 100) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (self.gameScreen[0] - 115, 35))
        img = pygame.image.load("images/" + str((timp%100) // 10) + str((timp%100) // 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (self.gameScreen[0] - 85, 35))
        img = pygame.image.load("images/" + str(timp % 10) + str(timp % 10) + ".png")
        img = pygame.transform.scale(img, (30, 30))
        self.screen.blit(img, (self.gameScreen[0] - 55, 35))

    def loadImages(self):
        self.images = {}
        for file in os.listdir("images"):
            if not file.endswith(".png"):
                continue
            image = pygame.image.load("images/" + file)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[file.split(".")[0]] = image

    def getImage(self, piece):
        string = None
        if piece.getClicked():
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]

    def handleClick(self, position, rightClick):
        if self.board.getLost():
            return
        index = (position[1] - 100) // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)