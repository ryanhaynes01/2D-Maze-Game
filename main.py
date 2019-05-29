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
        self.initX = 10
        self.initY = 10
        self.display = gameScreen
        self.idleAnimation = pygame.image.load("bin/sprites/adventurer-idle-00.png") # loads player sprite from bin

    def playerDraw(self):
        self.display.blit(self.idleAnimation, (self.initX, self.initY))

    def playerMovement(self, pressedKeys):
        if pressedKeys[pygame.K_RIGHT] and self.initX < WIDTH - 5 - 50: # moves player right if in boundary
            self.initX += 4
        if pressedKeys[pygame.K_LEFT] and self.initX > 5:               # moves player left if in boundary
            self.initX -= 4
        if pressedKeys[pygame.K_UP] and self.initY > 5:                 # moves player up if in boundary
            self.initY -= 4
        if pressedKeys[pygame.K_DOWN] and self.initY < HEIGHT - 5 - 37: # moves player down if in boundary
            self.initY += 4
        
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
            self.display.fill((0, 0, 0))      # refreshes background
            self.player.playerDraw()          # player blit update
            self.gameEdge()                   # keeps screen edge updated
            self.draw()                       # update screen for all blits
            clock.tick(self.FPS)              # fps limit set
            for event in pygame.event.get():  # fetches all events from pygame
                if event.type == pygame.QUIT: # if the x is pressed, close
                    self.gameState = False    # break the event loop
                print(event)                  # show events for debug
            keys = pygame.key.get_pressed()
            self.player.playerMovement(keys)

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
    
