from StaticObject import bigWall
from StaticObject import AntiGravityPlate
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

        #subtract 10 so pylons won't spawn inside walls
        self.makeRndPylons( self.game, pylons, (mapX - 10), (mapY - 10) )
        #self.makePylon( self.game, 100, 0, 0)
        
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

    def makeBoundaryWalls(self, game, MapX = 100.0, MapY = 100.0, WallLength = 50.0 ):
        WALLS = range(1, int(2*(MapX / WallLength ))+1)
        for Wall in WALLS:
            BigWall1 = bigWall(game)
            BigWall1.setPos( Vec3(-MapX + (WallLength*Wall)-(WallLength / 2) , -MapY, 0) )
            BigWall2 = bigWall(game)
            BigWall2.setPos( Vec3(-MapX + (WallLength*Wall)-(WallLength / 2) , +MapY, 0) )
            BigWall3 = bigWall(game)
            BigWall3.setRotation( 90 )
            BigWall3.setPos( Vec3(-MapX , -MapY + (WallLength*Wall)-(WallLength / 2), 0) )
            BigWall4 = bigWall(game)
            BigWall4.setRotation( 90 )
            BigWall4.setPos( Vec3(+MapX , -MapY + (WallLength*Wall)-(WallLength / 2), 0) )
            
            
    def makePylon(self, game, power, x, y):
        #spawns a new pylon and adds it to pylonList
        self.pylon = Pylon( game, power )
        self.pylon.setPos( Vec3(x, y, 0) )
        self.pylon.addToPylonList( self.pylonList )
        
        
    def makeRndPylons(self, game, amount, mapX, mapY):
        #create n amount of random powered pylons ( power is something between -game.MAX_PYLON_POWER and game.MAX_PYLON_POWER )
        for x in range(amount):
#            print str(x) + " loop"
            self.makePylon( game,
             random.randrange(-self.game.MAX_PYLON_POWER, self.game.MAX_PYLON_POWER),
             random.randrange( -mapX, mapX ), random.randrange( -mapY, mapY )
             )
        
    def makeBase(self, game, posY, posX = 0):
        #spawns a base
        self.base = Base( game )
        self.base.setPos( Vec3( posX, posY, 15), Vec3( posX, posY, 0) )

        return self.base

        #palauttaa basen ihan vaan siksi etta saa laitettua johonkin muuttujaan
        #ks. konstruktorissa self.base1 ja 2
        #  saadaan tunnistettua kumman base on kyseessa, 1-pelaajan vaiko 2  
    def makeAntiGravityPlate(self, game, mapX, mapY):
        #spawns an AntiGravityPlate
        self.agplate = AntiGravityPlate( game, mapX, mapY )
        self.agplate.setPos( Vec3( 0, 0, -5) )
        #return self.agplate
