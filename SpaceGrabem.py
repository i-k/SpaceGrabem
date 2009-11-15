'''

toimiiko tama kommenttina??

SpaceGrab'Em
Versio: 0.01


'''

from pandac.PandaModules import (
<<<<<<< HEAD:SpaceGrabem.py
  AmbientLight,
  DirectionalLight,
  PointLight,
  NodePath,
  Vec3,
  Vec4,
  Point3,
  Quat,
  OdeUtil,
  OdeWorld,
  OdeHashSpace,
  OdeJointGroup,
  OdeMass,
  OdeBody,
  OdeSphereGeom,
  OdeBoxGeom,
  BitMask32,
=======
#  AmbientLight,
  DirectionalLight,
#  PointLight,
#  NodePath,
  Vec3,
  Vec4,
#  Point3,
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
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py
  TextNode
)

from direct.gui.OnscreenText import OnscreenText
import direct.directbase.DirectStart


<<<<<<< HEAD:SpaceGrabem.py

import ShipTypes
import CollectibleTypes
=======
from Base import Base
import ShipTypes
import CollectibleTypes
import StaticObject
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py

class Game:

    HUD_TEXT_SCALE = 0.1
    UPDATE_RATE = 1/60.0

    def __init__(self):
<<<<<<< HEAD:SpaceGrabem.py
=======
        base.disableMouse()
        base.camera.setPos(0,0,240)
        base.camera.lookAt(0,0,0)
       
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py
        self.LoadHUD()
        self.loadPhysics()
        self.loadLights()
        
<<<<<<< HEAD:SpaceGrabem.py
        #self.wall = Wall(self)
        #self.wall.setPos( Vec3( 5, 0, 0) )
        
        self.ship1 = ShipTypes.Ship_2(self, Vec4(0.0, 0.0, 0.2, 0))
        self.ship2 = ShipTypes.Ship_1(self, Vec4(0.6, 0.0, 0.0, 0))
=======
        self.Base1 = Base(self)
        self.Base1.setPos( Vec3( 0, 50, 0))
        #self.Base2 = Base(self)
        self.wall = StaticObject.bigWall(self)
        self.wall.setPos( Vec3( 50, (-50), 0) )
        self.wall.setRotation( 20 )
        #alustaa tyhjan listan
        self.shipList = []
        self.ship1 = ShipTypes.Ship_2(self, Vec4(0.0, 0.0, 0.2, 0))
        
        self.ship2 = ShipTypes.Ship_1(self, Vec4(0.6, 0.0, 0.0, 0))
        
        #lisataan alukset listaan
        self.ship1.addShipToList(self.shipList)
        self.ship2.addShipToList(self.shipList)

        ##katsotaan saako toimimaan listana gamelooppiin -- saa
       ##self.shipList = [self.ship1, self.ship2]
        
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py
        self.ship2.setPos( Vec3(10, 10, 0) )
        
        
        self.setKeys()
        
        self.pallo = CollectibleTypes.Pallo(self, Vec4(0.0, 0.3, 0.0, 0))
        self.pallo.setPos( Vec3(0, 20, 0) )
        self.pallo2 = CollectibleTypes.Pallo(self, Vec4(0.0, 0.3, 0.0, 0))
        self.pallo2.setPos( Vec3(30, 20, 0) )
        
<<<<<<< HEAD:SpaceGrabem.py
=======
        self.collectibleList = [self.pallo, self.pallo2]
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py
 
        
        base.setBackgroundColor(0,0,0.0,0)
        
        taskMgr.add(self.loop, 'game loop')
        
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

        base.accept('w', self.ship2.thrustOn)
        base.accept('w-up', self.ship2.thrustOff)
        base.accept('a', self.ship2.thrustLeftOn)
        base.accept('a-up', self.ship2.thrustLeftOff)
        base.accept('d', self.ship2.thrustRightOn)
        base.accept('d-up', self.ship2.thrustRightOff) 
        base.accept('s', self.ship2.thrustBackOn)
        base.accept('s-up', self.ship2.thrustBackOff) 

        
        
        
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
        self.physicsSpace = OdeHashSpace()
        self.physicsSpace.setAutoCollideWorld(self.physicsWorld)
        self.contactGroup = OdeJointGroup()
        self.physicsSpace.setAutoCollideJointGroup(self.contactGroup)

    def LoadHUD(self):
        self.winnerText = OnscreenText(
            text = "Tekstia, tekstia, tekstia",
            fg = (1,1,1,1),
            pos = (-0.25, 0),
            align = TextNode.ALeft,
            scale = Game.HUD_TEXT_SCALE
        )
        self.winnerText.hide()

    def loadLights(self):
        light1 = DirectionalLight('light1')
        lightNode1 = render.attachNewNode(light1)
        light1.setDirection( Vec3(-1, 0.5, -0.25) )
        light1.setColor( Vec4(0.5, 0.9, 0.9, 0) )
        render.setLight(lightNode1)
        
<<<<<<< HEAD:SpaceGrabem.py
        
        
    def loop(self, task):
        self.ship1.applyForces()
        self.ship2.applyForces()
        self.physicsSpace.autoCollide()
        self.pallo.hitShips(self.ship1, self.ship2)
        self.pallo2.hitShips(self.ship1, self.ship2)
       # self.wall.osuminen(self.ship1)
        self.physicsWorld.quickStep(Game.UPDATE_RATE)
        self.ship1.update(Game.UPDATE_RATE)
        self.ship2.update(Game.UPDATE_RATE)
        self.pallo.update(Game.UPDATE_RATE)
        self.pallo2.update(Game.UPDATE_RATE)
=======
    #checks all collectibles for possible collisions with ships
    def checkAllCollectibles(self):
        for collectible in self.collectibleList:
            collectible.hitShips(self.shipList)

    #updates all collectible positions
    def updateAllCollectibles(self):
        for collectible in self.collectibleList:
            collectible.update(Game.UPDATE_RATE)
    
    #apply forces to all collectibles    
    ## def applyForceAllCollectibles(self):
        ## for collectible in self.collectibleList:
            ## collectible.applyForces()
    
    def applyForceAllShips(self):
        for ship in self.shipList:
            ship.applyForces()
            
    #updates all ship positions
    def updateAllShips(self):
        for ship in self.shipList:
            ship.update(Game.UPDATE_RATE)
        
        
    def loop(self, task):
        self.applyForceAllShips()
        self.physicsSpace.autoCollide()
        self.checkAllCollectibles()
        self.Base1.osuminen(self.ship1)
        self.physicsWorld.quickStep(Game.UPDATE_RATE)
        self.updateAllShips()
        self.updateAllCollectibles()
>>>>>>> 58af490611cf141600d95927f7ab641fe8f7171a:SpaceGrabem.py
        self.contactGroup.empty()
        return task.cont






        











## class Wall(GameObject):

    ## def __init__(self, game):
        ## self.game = game
        
        
        ## #self.visualNode = NodePath('Visual node')
        ## #self.visualNode.reparentTo(render)
        ## #model = loader.loadModel('testipalikka.egg')
        ## #model.reparentTo(self.visualNode)        

        ## self.body = OdeBody(game.physicsWorld)
        ## self.mass = OdeMass()
        ## self.mass.setBox(100,10,10,10)
        ## self.body.setMass(self.mass)
        ## self.body.setGravityMode(False)
        
        
        ## self.collGeom = OdeBoxGeom( self.game.physicsSpace, 100, 3, 10)
        ## self.collGeom.setBody(self.body)
        ## self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        ## self.collGeom.setCollideBits( BitMask32(0xffffffff) )
        
      ## #testiluokka, kertoo jos ship1 osuu seinaan  
    ## def osuminen(self, ship1):
         ## if OdeUtil.areConnected(ship1.body, self.body):
 
            ## print "sdfgfdhgdfhxfhdhghcfh"
            ## print "ship1 xdfhgxdgxdgfbcdll!!"
        
        



game = Game()
