import pygame

WIDTH, HEIGHT = 800, 600

class windowSetup:
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.caption = "2D Maze Game"

    def create(self):                                                    # game screen creation for game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

class playerHandler:
    def __init__(self, gameScreen):
        self.initX = WIDTH - (WIDTH + 5)
        self.initY = HEIGHT - 5 - 37
        self.display = gameScreen
        self.isJump = False
        self.jumpCount = 10
        self.idleAnimation = pygame.image.load("bin/sprites/adventurer-idle-00.png") # loads player sprite from bin
        self.animation = self.idleAnimation

    def playerDraw(self, animation):
        self.display.blit(animation, (self.initX, self.initY))

    def playerJump(self):                                   # very basic jumping mechanic
        if self.isJump:                                     # if true, able to 
            if self.jumpCount >= -10:                       # maintains parabolic motion from -10 to 10 (x variable)
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.initY -= self.jumpCount**2 * 0.1 * neg # quadratic for parabolic motion
                self.jumpCount -= 1
            else:
                self.isJump = False                         # stop the jump
                self.jumpCount = 10                         # reset jumpCount

    def playerMovement(self, pressedKeys):
        if pressedKeys[pygame.K_RIGHT] and self.initX < WIDTH - 5 - 50:      # moves player right if in boundary
            self.initX += 4
            self.animation = self.idleAnimation                              # sets animation for moving right
        if pressedKeys[pygame.K_LEFT] and self.initX > 5:                    # moves player left if in boundary
            self.initX -= 4
            self.animation = pygame.transform.flip(self.idleAnimation, 1, 0) # transforms right animation for moving left
        if pressedKeys[pygame.K_UP] and self.initY > 5:                      # moves player up if in boundary
            self.initY -= 4
        if pressedKeys[pygame.K_DOWN] and self.initY < HEIGHT - 5 - 37:      # moves player down if in boundary
            self.initY += 4
        if pressedKeys[pygame.K_SPACE]:
            self.isJump = True
            self.playerJump()
        self.playerDraw(self.animation)                                      # blit player to screen
        
class eventHandler:
    def __init__(self, gameScreen, game):
        self.FPS = 60
        self.display = gameScreen
        self.gameState = game
        self.player = playerHandler(self.display)

    def gameEdge(self):
        gameScreen = self.display
        edgeSize = 5
        pygame.draw.rect(gameScreen, (211,211,211), (0, 0, WIDTH, edgeSize))             # top rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (0, 0, edgeSize, HEIGHT))            # left rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (WIDTH-edgeSize, 0, WIDTH, HEIGHT))  # right rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (0, HEIGHT-edgeSize, WIDTH, HEIGHT)) # bottom rectangle
        self.display = gameScreen

    def draw(self):
        pygame.display.update() # draws everything blit to screen at once

    def events(self):
        clock = pygame.time.Clock()           # clock is declared for fps limit
        while self.gameState:
            clock.tick(self.FPS)              # fps limit set
            for event in pygame.event.get():  # fetches all events from pygame
                if event.type == pygame.QUIT: # if the x is pressed, close
                    self.gameState = False    # break the event loop
            keys = pygame.key.get_pressed()
            self.display.fill((0, 0, 0))      # refreshes background
            self.gameEdge()                   # keeps screen edge updated
            self.player.playerMovement(keys)
            self.draw()                       # update screen for all blits


def main():
    game = True
    displayCreation = windowSetup()                           # initialises windowSetup
    displayCreation.create()                                  # window is made
    eventUpdates = eventHandler(displayCreation.window, game) # initialises eventHandler
    while game:
        eventUpdates.events()                                 # interates events 
        game = eventUpdates.gameState                         # makes gamestate global
    pygame.quit()
    pass

if __name__ == '__main__':
    main()
    
