import pygame

WIDTH = 800
HEIGHT = 600

class windowSetup:
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.caption = "2D Maze Game"

    def create(self):                                                    # game screen creation for game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

class eventHandler:
    def __init__(self, gameScreen, game):
        self.FPS = 60
        self.display = gameScreen
        self.gameState = game

    def gameEdge(self):
        gameScreen = self.display
        pygame.draw.rect(gameScreen, (211,211,211), (0, 0, WIDTH, 10))              # top rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (0, 0, 10, HEIGHT))             # left rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (WIDTH-10, 0, WIDTH, HEIGHT))   # right rectangle
        pygame.draw.rect(gameScreen, (211,211,211), (0, HEIGHT-10, WIDTH, HEIGHT))  # bottom rectangle
        pygame.display.update()                                                     # draws rectangles to screen
        self.display = gameScreen

    def events(self):
        self.gameEdge()
        clock = pygame.time.Clock()           # clock is declared for fps limit
        while self.gameState:
            clock.tick(self.FPS)              # fps limit set
            for event in pygame.event.get():  # fetches all events from pygame
                if event.type == pygame.QUIT: # if the x is pressed, close
                    self.gameState = False    # break the event loop
                print(event)                  # show events for debug

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
    
