import pygame
from Enemy import Enemy

class Wave:

    # Constructor
    def __init__(self, aEnemyW, aEnemyH, aEnemySpeed, aNumEnemies, aTimeBetweenSpawns, aWaypointList) -> None:
        """Constructor

        Args:
            aEnemyW (int): width of an enemy
            aEnemyH (int): height of an enemy
            aEnemySpeed (float): speed that enemy will move
            aNumEnemies (int): The number of enemies in the wave
            aTimeBetweenSpawns (float): Number of ms between enemy spawns
            aWaypointList (list of pygame Vector2 objects): List of waypoints for enemies to move between
        """
        self.enemyW = aEnemyW
        self.enemyH = aEnemyH
        self.enemySpeed = aEnemySpeed
        self.numEnemies = aNumEnemies
        self.timeBetweenSpawns = aTimeBetweenSpawns
        # make it a copy so the original waypoint list is not edited
        self.waypointList = aWaypointList.copy()

        # get starting position
        self.startingX = self.waypointList[0].x
        self.startingY = self.waypointList[0].y

        # make list to store enemies
        self.enemyList = []

        # total number of enemies already spawned in current wave
        self.numSpawnedEnemies = 0

        # time object to regulate how many enemies have been spawned
        self.clock = pygame.time.Clock()

        # amount of time since last enemy was spawned
        self.timeSinceLastSpawn = 0

    # enemy spawn function
    def spawn(self):
        # if you should still spawn enemies
        if self.numSpawnedEnemies < self.numEnemies:
            # the time since the last time "tick" was called
            dt = self.clock.tick() 

            self.timeSinceLastSpawn += dt
            # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
            if self.timeSinceLastSpawn > self.timeBetweenSpawns:
                # spawn enemy
                self.enemyList.append(Enemy(self.startingX,
                                            self.startingY,
                                            self.enemyW,
                                            self.enemyH,
                                            self.enemySpeed,
                                            self.waypointList))

                # keep track of total number spawned
                self.numSpawnedEnemies += 1

                # reset timekeeper var
                self.timeSinceLastSpawn = 0

    # handle enemies
    def handleEnemies(self, aSurface) -> None:
        """draws all the enemies and moves them

        Args:
            aSurface (pygame Surface object): surface to draw on
        """
        for enemy in self.enemyList:
            enemy.renderHitbox(aSurface)
            enemy.updatePos()

        