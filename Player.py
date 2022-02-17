import pygame
from pygame import image



class Player:
    def __init__(self, startX, startY, width, height, startHealth, startSpeed, image):
        """Constructor function

        Args:
            startX (int): starting x pos
            startY (int): starting y pos
            width (int): width
            height (int): height
            startHealth (int): starting health
            startSpeed (int): starting speed
            image (pygame Surface): Image to be drawn
        """
        self.width = width
        self.height = height
        self.health = startHealth
        self.speed = startSpeed
        self.image = image

        self.hitbox = pygame.Rect(startX, startY, self.width, self.height)

        # scale the yellow ship image
        self.image = pygame.transform.scale(self.image, (width,height))


    def display(self, aSurface):
        """Displays the player at the given surface

        Args:
            aSurface (pygame Surface): 
        """
        aSurface.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def displayHealth(self, x, y, aSurface, aFont, aColor):
        """Displays this player's health at the given x and y and on the given surface

        Args:
            x (int): x pos of the score
            y (int): y pos of the score
            aSurface (pygame Surface): surface of the game window
            aFont (pygame.font Sysfont object): the font the score should be in
            aColor (tuple of RGB vals): the color the font should be in
        """
         # make the objects to be rendered
        healthObject = aFont.render(str(self.health), 1, aColor)

        # render the objects
        aSurface.blit(healthObject, (x,y))
        


    def moveRight(self):
        """moves the player right depending on their speed
        """
        self.hitbox.x += self.speed

    def moveLeft(self):
        """moves the player left depending on their speed
        """
        self.hitbox.x -= self.speed

    def moveUp(self):
        """moves the player up depending on their speed
        """
        self.hitbox.y -= self.speed

    def moveDown(self):
        """moves the player down depending on their speed
        """
        self.hitbox.y += self.speed

    def loseHealth(self) -> None:
        """subtracts the player's health by 1
        """
        self.health -= 1



    