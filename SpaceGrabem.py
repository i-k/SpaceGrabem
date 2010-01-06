'''

toimiiko tama kommenttina??

SpaceGrab'Em
Versio: 0.6

Yleinen TODO: Raketin hitboxit kunnolla, aaniefektit, taustakuva
Modelit ja niiden teksturointi

'''

from pandac.PandaModules import (
 # AmbientLight,
  DirectionalLight,
  PointLight,
#  NodePath,
  Vec3,
  Vec4,
  Point3,
#  Quat,
#  OdeUtil,
  OdeWorld,
  OdeHashSpace,
  OdeJointGroup,
#  OdeMass,
#  OdeBody,
#  OdeSphereGeom,
#  OdeBoxGeom,
#  BitMask32,
  TextNode
)

from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
import direct.directbase.DirectStart
from direct.filter.CommonFilters import CommonFilters


#from Base import Base
#from Pylon import Pylon
from Map import Map
import ShipTypes
import CollectibleTypes
#import StaticObject
import math

class Game():

    HUD_TEXT_SCALE = 0.04
    UPDATE_RATE = 1/60.0
    MAX_PYLON_POWER = 50

    def __init__(self):
        base.disableMouse()
        base.camera.setPos(0,0,640)
        base.camera.lookAt(0,0,0)
        
        self.loadPhysics()
        self.loadLights()
        
        #map x boundary, map y boundary, amount of pylons
        self.map = Map(self, 150.0, 150.0, 7)

        self.shipList = []
        self.ship1 = ShipTypes.Ship_1(self, Vec4(0.6, 0.0, 0.0, 0.0))
        self.ship2 = ShipTypes.Ship_2(self, Vec4(0.0, 0.0, 0.6, 0.0))
        self.ship1.setPos( Vec3(0, 120, 0) )
        self.ship2.setPos( Vec3(0, -120, 0) )    
        self.shipList.append(self.ship1)
        self.shipList.append(self.ship2)
        
        self.LoadHUD()
        
        self.setKeys()
        
        self.collectibleList = []
        self.pallo = CollectibleTypes.Pallo(self, Vec4(0.0, 0.3, 0.0, 0))
        self.pallo.setPos( Vec3(0, 20, 0) )
        self.pallo.addToCollectibleList(self.collectibleList)
        
        #self.pallo2 = CollectibleTypes.Pallo(self, Vec4(0.0, 0.3, 0.0, 0))
        #self.pallo2.setPos( Vec3(30, 20, 0) )
        #self.pallo2.addToCollectibleList(self.collectibleList)
        
        b=OnscreenImage(parent=render2d, image="Geminid.jpg")
        base.cam.node().getDisplayRegion(0).setSort(20)
        
        base.setBackgroundColor(0,0,0.0,0)
        
        self.collisionSfx = loader.loadSfx("shipcollision.wav")
        self.goalSfx = loader.loadSfx("goal.wav")
        self.victorySfx = loader.loadSfx("victory.mp3")
        self.collision2Sfx = loader.loadSfx("pyloncollision.wav")
        
        filters = CommonFilters(base.win, base.cam)
        render.setShaderAuto()
        
        taskMgr.add(self.loop, 'game loop')
        taskMgr.add( self.chaseBallsAround, name='Simple AI', sort=None, extraArgs=(self.ship1, self.ship2, self.collectibleList, self.map.getBase1()), priority=None, uponDeath=None, appendTask=True, taskChain=None, owner=None)
        
        run()
        
    def setKeys(self):
        base.accept('arrow_up', self.ship1.thrustOn)
        base.accept('arrow_up-up', self.ship1.thrustOff)
        base.accept('arrow_left', self.ship1.thrustLeftOn)
        base.accept('arrow_left-up', self.ship1.thrustLeftOff)
        base.accept('arrow_right', self.ship1.thrustRightOn)
        base.accept('arrow_right-up', self.ship1.thrustRightOff) 
        base.accept('arrow_down', self.ship1.thrustBackOn)
        base.accept('arrow_down-up', self.ship1.thrustBackOff) 
        base.accept('rshift', self.ship1.releaseBall)

        base.accept('w', self.ship2.thrustOn)
        base.accept('w-up', self.ship2.thrustOff)
        base.accept('a', self.ship2.thrustLeftOn)
        base.accept('a-up', self.ship2.thrustLeftOff)
        base.accept('d', self.ship2.thrustRightOn)
        base.accept('d-up', self.ship2.thrustRightOff) 
        base.accept('s', self.ship2.thrustBackOn)
        base.accept('s-up', self.ship2.thrustBackOff) 
        base.accept('q', self.ship2.releaseBall)
        
        
        
    def loadPhysics(self):
        self.physicsWorld = OdeWorld()
        self.physicsWorld.initSurfaceTable(1)
        self.physicsWorld.setSurfaceEntry(
          0,
          0,
          1.0, # u
          0.35, # elasticity
          0.01, # minimum threshold for physical movement
          0.01,
          0.00000001, # softening
          0.01,
          0.01 # damping
        )

        self.physicsWorld.setGravity(0, 0, -20)

        self.physicsSpace = OdeHashSpace()
        self.physicsSpace.setAutoCollideWorld(self.physicsWorld)
        self.contactGroup = OdeJointGroup()
        self.physicsSpace.setAutoCollideJointGroup(self.contactGroup)

    def LoadHUD(self):
        self.player1HUD = OnscreenText(
            text = "Player 1: " + str( self.ship1.getPoints() ),
            fg = (1,1,1,1),
            #pos = ( x, y )
            pos = (0.7,0.9),
            align = TextNode.ALeft,
            scale = Game.HUD_TEXT_SCALE
        )
        
        self.player2HUD = OnscreenText(
            text = "Player 2: " + str( self.ship2.getPoints() ),
            fg = (1,1,1,1),
            pos = (-0.7,0.9),
            align = TextNode.ALeft,
            scale = Game.HUD_TEXT_SCALE
        )
        
        self.winnerText = OnscreenText(
            text = "Tekstia, tekstia, tekstia",
            fg = (1,1,1,1),
            pos = (-0.25, 0),
            align = TextNode.ALeft,
            scale = Game.HUD_TEXT_SCALE
        )
        self.winnerText.setZ(600)
        self.winnerText.hide()

    def updateHUD(self):
        self.player1HUD.setText( "Player 1: " + str( self.ship1.getPoints() ) )
        self.player2HUD.setText( "Player 2: " + str( self.ship2.getPoints() ) )
        if (self.ship1.getPoints() > 9):
            self.winnerText.show()
            self.winnerText.setText( "Player 1 won " + str(self.ship1.getPoints()) + "-" + str(self.ship2.getPoints()))
            self.victorySfx.play()
#            self.Pause()
        if (self.ship2.getPoints() > 9):
            self.winnerText.show()
            self.winnerText.setText( "Player 2 won " + str(self.ship2.getPoints()) + "-" + str(self.ship1.getPoints()))
            self.victorySfx.play()


    def loadLights(self):
        light1 = DirectionalLight('light1')
        lightNode1 = render.attachNewNode(light1)
        light1.setDirection( Vec3(-1, 0.5, -0.25) )
        light1.setColor( Vec4(0.6, 0.6, 0.6, 0) )
        render.setLight(lightNode1)
        
    #checks all collectibles for possible collisions with ships
    def checkAllCollectibles(self, shipList):
        for collectible in self.collectibleList:
            collectible.hitShips(shipList)

    #updates all collectible positions
    def updateAllCollectibles(self):
        for collectible in self.collectibleList:
            collectible.update(Game.UPDATE_RATE)
    
    def applyForceAllShips(self, shipList):
        for ship in shipList:
            ship.applyForces()
            
    #updates all ship positions
    def updateAllShips(self, shipList):
        for ship in shipList:
            ship.update(Game.UPDATE_RATE)
        shipList[0].shipsCollide(shipList[1])
            
    #checks all pylons for possible collisions with ships
    def checkAllPylons(self, pylonList, shipList):
        for pylon in pylonList:
            pylon.checkCollisionList(shipList)
        
        
    def loop(self, task):
        self.applyForceAllShips(self.shipList)
        self.physicsSpace.autoCollide()
        self.checkAllCollectibles(self.shipList)
        self.map.getBase1().checkCollision(self.ship1, self.collectibleList)
        self.map.getBase2().checkCollision(self.ship2, self.collectibleList)
        self.checkAllPylons(self.map.getPylonList(), self.shipList)
        self.physicsWorld.quickStep(Game.UPDATE_RATE)
        self.updateAllShips(self.shipList)
        self.updateAllCollectibles()
        self.contactGroup.empty()
        return task.cont
        
    def chaseBallsAround(self, chaser, enemy, chaseList, base, task):
        pos = chaser.getPos()
        nearestNormedPos = 1e10000 #represents infinity
        nearestRelPos = [0,0]
        if chaser.hasBall():
            basePos = base.getPos()
            nearestRelPos = [ pos[0] - basePos[0], pos[1] - basePos[1] ]
        elif enemy.hasBall():
            enemyPos = enemy.getPos()
            nearestRelPos = [ pos[0] - enemyPos[0], pos[1] - enemyPos[1] ]
        else:
            for collectible in chaseList:
                cPos = collectible.getPos()
                relPos = [ pos[0] - cPos[0], pos[1] - cPos[1] ]
                if (math.fabs(relPos[0]) + math.fabs(relPos[1])) < nearestNormedPos:
                    nearestNormedPos = math.fabs(relPos[0]) + math.fabs(relPos[1])
                    nearestRelPos = relPos
        if nearestRelPos[0] > 0:
            chaser.thrustRightOff()
            chaser.thrustLeftOn()
        elif nearestRelPos[0] < 0:
            chaser.thrustLeftOff()
            chaser.thrustRightOn()
        if nearestRelPos[1] < 0:
            chaser.thrustBackOff()
            chaser.thrustOn()
        elif nearestRelPos[1] > 0:
            chaser.thrustOff()
            chaser.thrustBackOn()
        else:
            chaser.thrustOff()
            chaser.thrustBackOff()
        return task.cont
    
game = Game()
