from xmlrpc.client import boolean
import pygame

from Bullet import Bullet

class BulletList:

    # Constructor
    def __init__(self) -> None:
        # list of bullets to store
        self.bulletList = []
        
        pass


    def checkCollision(self, aRect) -> boolean:
        """Returns true if the bullet is colliding with given aRect. Otherwise, returns false

        Args:
            aRect (pygame rect): hitbox of object to check collision against
        """
        pass