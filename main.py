############
# imports
############
import pygame

from Player import Player

###########
# Global vars
###########

# size of the game window
WIDTH = 1000
HEIGHT = 700

# set the max frame rate of the game
FPS = 60

# window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# naming the game window
pygame.display.set_caption("Galaga Pygame")

#### Loading image assets
# load the image for the background
backgroundImg = pygame.image.load("Assets/space.png")
# scale the yellow ship image
backgroundImg = pygame.transform.scale(backgroundImg, (WINDOW.get_width(),WINDOW.get_height()))


############
# Function definitions
############

def main():
    """Runs the game- includes the game loop
    """
    # clock object to regulate the framerate
    clock = pygame.time.Clock()

    # boolean representing if the game should keep looping
    isRunning = True

    # Player instantiation
    PLAYER1 = Player(200, 200, 75, 75, 3, 10, pygame.image.load("Assets/spaceship_yellow.png"))
    PLAYER1.image = pygame.transform.rotate(PLAYER1.image, 180)


    # game loop
    while isRunning:
        
        # run at given framerate
        clock.tick(FPS)

        # for all the game events
        for event in pygame.event.get():
            
            # if user presses the x key
            if event.type == pygame.QUIT:
                isRunning = False

        PLAYER1.display(WINDOW)

        # update display
        pygame.display.update()



















########
# run main
########

if __name__ == "__main__":
   main()