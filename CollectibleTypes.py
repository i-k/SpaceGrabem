import random
from pandac.PandaModules import (
#  AmbientLight,
#  DirectionalLight,
  PointLight,
  NodePath,
  Vec3,
#  Vec4,
  Point3,
#  Quat,
  OdeUtil,
#  OdeWorld,
#  OdeHashSpace,
#  OdeJointGroup,
  OdeMass,
  OdeBody,
  OdeSphereGeom,
  OdeBoxGeom,
  BitMask32
#  TextNode
)

from Collectible import Collectible

class Pallo(Collectible):
    
 #   COLLECTIBLE_TYPE = 'PointBall'
 #   VALUE = 1
 #   DRAIN = 20

    
    def __init__(self, game, color, value = 1, drain = 20):
        self.game = game
        self.VALUE = value
        self.DRAIN = drain
        
        #self.idnumber = id
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('Ball2.egg')
        model.setScale(2.5)
        model.reparentTo(self.visualNode)

        plight = PointLight('plight')
        plight.setPoint( Point3(0, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = model.attachNewNode(plight)
        model.setLight(plightNodePath)

        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)

        self.body.setGravityMode(True)

        #self.body.setGravityMode(False)
        #self.juttu = OdeUtil()
        
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 3.5)
        self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
    
    def getValue(self):
        return self.VALUE
    
    def hitShips(self, shipList):
        
        for ship in shipList:
            if OdeUtil.areConnected(ship.body, self.body) and not ship.hasBall():
                            
                self.PowerUpEffect(ship)

    def PowerUpEffect(self, ship):
     #   ship.mass.add(self.mass)
        ship.addPower(-(self.DRAIN))
        ship.gotBall(self)
        self.hideObject()
        
        #print player
        print ship.SHIP_TYPE + " lost " + str(self.DRAIN) + " power!!"
        
    def Restore(self, ship):
      #  ship.mass.add(self.mass)
        ship.addPower(self.DRAIN)
        self.showObject()
        #self.setPos( Vec3(random.randrange(30), random.randrange(40), 0))
        #ship.dropBall()
        #print player
        print ship.getShipType() + " regained 20 power!!"
        
  #  def releaseForces(self, ship):
