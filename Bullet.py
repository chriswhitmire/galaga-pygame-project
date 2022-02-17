import pygame

class Bullet:
    def __init__(self, startX, startY, diameter, speed, colorTuple, isMovingUp):
        """Constructor

        Args:
            startX (int): starting x pos
            startY (int): starting y pos
            diameter (int): diameter
            speed (int): speed the bullet moves
            colorTuple (tuple of ints): tuple of RGB values (0-255)
            isMovingUp (bool): if true, moves up. if false, moves down
        """
        self.diameter = diameter
        self.speed = speed
        self.color = colorTuple
        self.isMovingUp = isMovingUp

        self.hitbox = pygame.Rect(startX, startY, diameter, diameter)

    def display(self, aSurface):
        """displays the bullet

        Args:
            aSurface (pygame Surface): surface to draw the bullet on
        """
        pygame.draw.circle(aSurface, self.color,(self.hitbox.x, self.hitbox.y), self.diameter)
    
    def move(self):
        """moves the bullet
        """
        if self.isMovingUp:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed