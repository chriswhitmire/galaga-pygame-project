import pygame

class Enemy:

    color = (255,255,255)

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
        # initialize vars
        self.hitbox = pygame.rect.Rect(x_, y_, w_, h_)
        self.speed = aSpeed
        self.waypointList = aWaypointList

        # get the starting position
        self.currentPos = self.waypointList[0]
        # get the index of the target position
        self.waypointIndex = 1
        
    def updatePos(self):

        # if you have not reached the last waypoint
        if self.waypointIndex < len(self.waypointList):
            
            # get the target pos
            targetPos = self.waypointList[self.waypointIndex]

            # if you have not reached the current position yet
            # then move towards the target
            if self.currentPos != targetPos:
                # get the velocity
                velocity = targetPos - self.currentPos
                # normalize the velocity to get a unit vector
                velocity = velocity.normalize()
                # update the current position so that it moves towards the target
                self.currentPos += (velocity*self.speed)

                # if it is close enough to the target, then move on to the next target
                if self.currentPos.distance_to(targetPos) <= self.speed:
                    self.waypointIndex += 1

            # update the hitbox position to match currentPos
            self.hitbox.x = self.currentPos.x
            self.hitbox.y = self.currentPos.y
    
    def renderHitbox(self, aSurface):
        """Displays the hitbox of the game object

        Args:
            aSurface (pygame surface object): surface to draw on
        """
        pygame.draw.rect(aSurface, self.color, self.hitbox, 1)
        
    
    