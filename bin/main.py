import pygame

class windowSetup:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.caption = "2D Maze Game"

    def create(self): # game screen creation for rest of the game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

class eventHandler:
    def __init__(self, gameScreen, game):
        self.FPS = 60
        self.display = gameScreen
        self.gameState = game

    def events(self):
        clock = pygame.time.Clock()           # clock is declared for fps limit
        while self.gameState:
            clock.tick(self.FPS)
            for event in pygame.event.get():  # fetches all events from pygame
                if event.type == pygame.QUIT: # if the x is press, close
                    self.gameState = False    # break the event loop
                print(event)                  # show events for debug

def main():
    game = True
    displayCreation = windowSetup()
    displayCreation.create()
    eventUpdates = eventHandler(displayCreation.window, game)
    while game:
        eventUpdates.events()
        game = eventUpdates.gameState
    pygame.quit()

if __name__ == '__main__':
    main()
    
