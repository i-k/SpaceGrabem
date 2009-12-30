from StaticObject import BigWall, AntiGravityPlate
#from StaticObject import AntiGravityPlate
from Base import Base
from Pylon import Pylon
import ShipTypes

import math, random

from pandac.PandaModules import (
  Vec3,
  Vec4
)


class Map:
    
    def __init__(self, game, mapX = 100.0, mapY = 100.0, pylons = 3):

        self.game = game
        self.pylonList = []

        self.walls = render.attachNewNode("Walls")

        #subtract 10 so pylons won't spawn inside walls
        self.makeRndPylons( self.game, pylons, (mapX - 10), (mapY - 10) )
        #self.makePylon( self.game, 100, 0, 0)
        self.makeRndWalls( self.game, pylons/2, (mapX - 10), (mapY - 10) )
        
        #subtract 10 so bases won't spawn inside walls
        self.base1 = self.makeBase( self.game, (mapY - 10) )
        self.base2 = self.makeBase( self.game, -(mapY - 10) )

        self.makeBoundaryWalls( self.game, mapX, mapY )

        self.makeAntiGravityPlate( self.game, (2*mapX), (2*mapY) )

        
    def getPylonList(self):
        return self.pylonList

    def getShiplist(self):
        return self.shipList
    
    def getBase1(self):
        return self.base1
    
    def getBase2(self):
        return self.base2

    def makeBoundaryWalls(self, game, mapX = 100.0, mapY = 100.0):
        wall1 = BigWall(game, 2*mapX)
        wall1.setPos( Vec3(0, -mapY, 0) )
        wall1.visualNode.reparentTo(self.walls)
        wall2 = BigWall(game, 2*mapX)
        wall2.setPos( Vec3(0, mapY, 0) )
        wall2.visualNode.reparentTo(self.walls)
        wall3 = BigWall(game, 2*mapY)
        wall3.setRotation( 90 )
        wall3.setPos( Vec3(-mapX , 0, 0) )
        wall3.visualNode.reparentTo(self.walls)
        wall4 = BigWall(game, 2*mapY)
        wall4.setRotation( 90 )
        wall4.setPos( Vec3(mapX , 0, 0) )
        wall4.visualNode.reparentTo(self.walls)
        
            
    def makePylon(self, game, power, x, y):
        self.pylon = Pylon( game, power )
        self.pylon.setPos( Vec3(x, y, 0) )
        self.pylon.addToPylonList( self.pylonList )
        
        
    def makeRndPylons(self, game, amount, mapX, mapY):
        #create n amount of random powered pylons ( power is something between -game.MAX_PYLON_POWER and game.MAX_PYLON_POWER )
        for x in range(amount):
            self.makePylon( game,
             random.randrange(-self.game.MAX_PYLON_POWER, self.game.MAX_PYLON_POWER),
             random.randrange( -mapX, mapX ), random.randrange( -mapY, mapY )
             )
             
    def makeRndWalls(self, game, amount, mapX, mapY, minWallWidth = 40.0, maxWallWidth=60.0):
        for x in range(amount):
            wall = BigWall( game, random.randrange(minWallWidth, maxWallWidth) )
            wall.setPos( Vec3(random.randrange( -mapX, mapX ), random.randrange( -mapY, mapY ), 0) )
            wall.visualNode.reparentTo(self.walls)
        
    def makeBase(self, game, posY, posX = 0):
        #spawns a base
        self.base = Base( game )
        self.base.setPos( Vec3( posX, posY, 15), Vec3( posX, posY, 0) )

        return self.base

        #ks. konstruktorissa self.base1 ja 2
        #  saadaan tunnistettua kumman base on kyseessa, 1-pelaajan vaiko 2  
    def makeAntiGravityPlate(self, game, mapX, mapY):
        self.agplate = AntiGravityPlate( game, mapX, mapY )
        self.agplate.setPos( Vec3( 0, 0, -5) )
