############
# imports
############
from random import random
import random
import pygame

from Player import Player
from Bullet import Bullet
from Wave import Wave
from WaveGenerator import WaveGenerator

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

    # waypointlist instantiation TESTING
    waypointList1 = [pygame.Vector2(-100,100), pygame.Vector2(WIDTH-200,100),
                     pygame.Vector2(200, 300), pygame.Vector2(WIDTH + 100, 300)]

    waypointList2 = [pygame.Vector2(-100,100), pygame.Vector2(100,100),
                     pygame.Vector2(300, 300), pygame.Vector2(500, 100),
                     pygame.Vector2(700, 300), pygame.Vector2(900, 100),
                     pygame.Vector2(1100, 300)]

    waypointList3 = [pygame.Vector2(WIDTH/2,-100), pygame.Vector2(WIDTH/2,HEIGHT/4),
                     pygame.Vector2(300, 300), pygame.Vector2(300, 100),
                     pygame.Vector2(700, 100), pygame.Vector2(700, 300),
                     pygame.Vector2(WIDTH/2,HEIGHT/4), pygame.Vector2(WIDTH/2,-100)]

    listOfWaypointLists = []
    listOfWaypointLists.append(waypointList1)
    listOfWaypointLists.append(waypointList2)
    listOfWaypointLists.append(waypointList3)

    # Wave instantiation TESTING
    waveZ = Wave(20, 20, 5, 3, 1000, waypointList1)
    waveSpike = Wave(20, 20, 5, 3, 1000, waypointList2)
    waveCircle = Wave(20, 20, 5, 3, 1000, waypointList3)

    # Wave generator instantiation TESTING
    waveGenerator1 = WaveGenerator(listOfWaypointLists, 5000 )

    # Player bullets
    playerBulletList = []

    # enemy shooting bullet vars
    timeBetweenEnemyShots = random.randint(1000,3000)
    timeSinceLastEnemyShot = 0
    enemyShootClock = pygame.time.Clock()

    # enemy bullet vars
    enemyBulletList = []

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

        # timer to keep track of when enemy should shoot a bullet
        enemyShotDT = enemyShootClock.tick()
        timeSinceLastEnemyShot += enemyShotDT

        if timeSinceLastEnemyShot > timeBetweenEnemyShots and len(waveGenerator1.activeWaves) > 0:
            # reset the timer
            timeSinceLastEnemyShot = 0
            # set a new random interval for the next bullet spawn
            timeBetweenEnemyShots = random.randint(200,3000)

            # get a random enemy from a random wave
            targetWave = waveGenerator1.activeWaves[random.randint(0, len(waveGenerator1.activeWaves) - 1)]
            if len(targetWave.enemyList) > 0:
                targetEnemy = targetWave.enemyList[random.randint(0, len(targetWave.enemyList)-1)]
                
                # spawn a new bullet at the enemies location
                enemyBulletList.append(Bullet(targetEnemy.hitbox.left+targetEnemy.hitbox.width,
                                            targetEnemy.hitbox.bottom,
                                            3,
                                            15,
                                            (255,0,0),
                                            False))

        # reset the background
        WINDOW.fill((0,0,0))
        
        # for every enemy bullet, render it and check for collision
        enemyBulletsToKeep = []
        for enemyBullet in enemyBulletList:
            enemyBullet.display(WINDOW)
            enemyBullet.move()

            # if the enemy bullet hits the player
            if (enemyBullet.hitbox.colliderect(PLAYER1.hitbox)):
                # subtract from the player's health
                PLAYER1.loseHealth()

            # if the enemy does not hit the player and
            # if the enemy bullet is not past the bottom of the window,
            # then keep it
            elif enemyBullet.hitbox.top < HEIGHT:
                enemyBulletsToKeep.append(enemyBullet)

        enemyBulletList = enemyBulletsToKeep

        
        # display the player
        PLAYER1.display(WINDOW)

        # check if you should generate a new wave
        waveGenerator1.makeWave()
        waveGenerator1.removeDeadWaves()
        print(len(waveGenerator1.activeWaves))

        # managing all the active waves
        for wave in waveGenerator1.activeWaves:
            wave.spawn()
            wave.handleEnemies(WINDOW)

        ### move and display every player bullet
        bulletsToKeep = []
        for bullet in playerBulletList:
            bullet.display(WINDOW)
            bullet.move()

            # for every wave
            for wave in waveGenerator1.activeWaves:
                # for every enemy in each wave
                for enemy in wave.enemyList:

                    # check if the enemy is hit by a bullet
                    if enemy.hitbox.colliderect(bullet.hitbox):
                        # change the enemy's color to red
                        enemy.color = (255,0,0)
                
            # only keep bullets that are still on the screen
            if bullet.hitbox.y > -10:
                bulletsToKeep.append(bullet)

        # make the active bullets the same as the bullets still on screen
        playerBulletList = bulletsToKeep

        # update display
        pygame.display.update()

########
# run main
########

if __name__ == "__main__":
   main()