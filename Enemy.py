import pygame

class Enemy:

    # Constructor
    def __init__(self, x_, y_, w_, h_, aSpeed, aWaypointList) -> None:
        """Constructor

        Args:
            x_ (int): initializes x pos
            y_ (int): initializes y pos
            w_ (int): initializes width
            h_ (int): initializes height
            aSpeed (float): initializes speed
            aWaypointList (TBD): [description]
        """
        self.hitbox = pygame.rect.Rect(x_, y_, w_, h_)
        self.speed = aSpeed

    def renderHitbox(self, aSurface):
        """Displays the hitbox of the game object

        Args:
            aSurface (pygame surface object): surface to draw on
        """
        pygame.draw.rect(aSurface, (255,0,0,20))
        
    
    