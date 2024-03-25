import pygame.transform


class Button():
    def __init__(self, pos, text_input, value=0):
        self.value = value
        self.image = pygame.image.load("images/0.png")
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = pygame.font.SysFont("Arial", 24)
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, "#AF0F0F")
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def returnValue(self):
        return self.value


