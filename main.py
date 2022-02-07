############
# imports
############
import pygame

from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from Wave import Wave

###########
# Global vars
###########

# size of the game window
WIDTH = 1000
HEIGHT = 700

# set the max frame rate of the game
FPS = 60

# amt of padding around the edge of the window that the player cannot move past
PADDING = 20

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

    # Enemy instantiation TESTING
    waypointList1 = [pygame.Vector2(100,100), pygame.Vector2(300, 500), pygame.Vector2(500, 200)]
    enemy1 = Enemy(100, 100, 100, 100, 10, waypointList1)

    # Wave instantiation TESTING
    wave1 = Wave(20, 20, 5, 3, 1000, waypointList1)

    # Player bullets
    playerBulletList = []


    # game loop
    while isRunning:
        
        # run at given framerate
        clock.tick(FPS)

        # for all the game events
        for event in pygame.event.get():
            
            # if user presses the x key in corner of window
            if event.type == pygame.QUIT:
                isRunning = False

            # if spacebar is pressed, then add a bullet to the player's bullet list
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        playerBulletList.append(Bullet(PLAYER1.hitbox.x + PLAYER1.hitbox.width/2, PLAYER1.hitbox.y, 5, 20, (255,255,0), True))


        ###### key presses
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

        # if the 'w' key is pressed
        if keysPressed[pygame.K_w] == True and PLAYER1.hitbox.top > PLAYER1.speed + PADDING:
            PLAYER1.moveUp()

        # if the 'a' key is pressed
        if keysPressed[pygame.K_a] == True and PLAYER1.hitbox.left > PLAYER1.speed + PADDING:
            PLAYER1.moveLeft()

        # if the 's' key is pressed
        if keysPressed[pygame.K_s] == True and PLAYER1.hitbox.bottom < WINDOW.get_height() - PLAYER1.speed- PADDING:
            PLAYER1.moveDown()

        # if the 'd' key is pressed
        if keysPressed[pygame.K_d] == True and PLAYER1.hitbox.right < WINDOW.get_width() - PLAYER1.speed - PADDING:
            PLAYER1.moveRight()

        
        # reset the background
        WINDOW.fill((0,0,0))
        
        # display the player
        PLAYER1.display(WINDOW)

        # display the enemy- TESTING
        #enemy1.renderHitbox(WINDOW)
        # update the position of the enemy
        #enemy1.updatePos()

        # Wave TESTING
        wave1.spawn()
        wave1.handleEnemies(WINDOW)

        ### move and display every player bullet
        bulletsToKeep = []
        for bullet in playerBulletList:
            bullet.display(WINDOW)
            bullet.move()

            # TODO change this to work with list of enemies
            # check if the bullet collides with the enemy- TEST
            for enemy in wave1.enemyList:

                if enemy.hitbox.colliderect(bullet.hitbox):
                    # change the enemy's color to red
                    enemy.color = (255,0,0)
            
            # only keep bullets that are still on the screen
            if bullet.hitbox.y > -10:
                bulletsToKeep.append(bullet)

        # make the active bullets the same as the bullets still on screen
        playerBulletList = bulletsToKeep

        print(len(playerBulletList))

        # update display
        pygame.display.update()

########
# run main
########

if __name__ == "__main__":
   main()