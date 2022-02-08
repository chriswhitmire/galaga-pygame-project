import pygame
from Wave import Wave

import random

class WaveGenerator:

    # Constructor
    def __init__(self, aListOfWaypointLists, aTimeBetweenWaveGenerations) -> None:
        """Constructor

        Args:
            aListOfWaypointLists (list of 2-element lists holding pygame Vector2 objects): list of paths of waypoints that enemies will follow
            aTimeBetweenWaves (int): time in ms between when a new wave is spawned
        """
        # list of predefined waypoint paths
        self.listOfWayPointLists = aListOfWaypointLists

        # stores active waves
        self.activeWaves = []

        # time between wave generations
        self.timeBetweenWaveGenerations = aTimeBetweenWaveGenerations

        # time object to regulate how often waves are generated
        self.timeSinceLastGeneration = 0
        self.clock = pygame.time.Clock()
        pass


    def generateRandomPredefinedWave(self, enemySize=50, enemySpeed=random.randint(5,10),
                                    numEnemies=random.randint(3,8),
                                    timeBetweenSpawns=random.randint(200,2000)):
        """Generates a wave with random stats. The waypoint list used is selected randomly
        from the predefined list saved with the object.

        Args:
            enemySize (int, optional): The width/height of the enemy. Defaults to 50.
            enemySpeed (int, optional): Speed of enemy. Defaults to random.randint(5,10).
            numEnemies (int, optional): Number of enemies in the wave. Defaults to random.randint(3,8).
            timeBetweenSpawns (int, optional): Time in ms between enemy spawns. Defaults to random.randint(200,2000).
        """
        randomIndex = random.randint(0, len(self.listOfWayPointLists) - 1)
        
        self.activeWaves.append(Wave(enemySize,
                                    enemySize,
                                    enemySpeed,
                                    numEnemies,
                                    timeBetweenSpawns, 
                                    self.listOfWayPointLists[randomIndex]))


    def makeWave(self):
        """Generates a new wave after some time has passed
        """
        # the time since the last time "tick" was called
        dt = self.clock.tick() 

        self.timeSinceLastGeneration += dt

        # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
        if self.timeSinceLastGeneration > self.timeBetweenWaveGenerations:
            self.generateRandomPredefinedWave()
            self.timeSinceLastGeneration = 0

            # make a random time to pass before the next wave spawns
            self.timeBetweenWaveGenerations = random.randint(4000,12000)


    def removeDeadWaves(self):
        """Removes all waves that do not have any enemies left in them
        """

        # list of waves to keep active
        wavesToKeep = []

        # only keep the waves that still have active enemies in them
        for wave in self.activeWaves:
            if len(wave.enemyList) != 0 or (wave.numSpawnedEnemies < wave.numEnemies):
                wavesToKeep.append(wave)

        # only keep appropriate waves
        self.activeWaves = wavesToKeep.copy()

    


