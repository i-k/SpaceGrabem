from pandac.PandaModules import (
# AmbientLight,
# DirectionalLight,
  PointLight,
  NodePath,
  Vec3,
# Vec4,
  Point3,
# Quat,
# OdeUtil,
# OdeWorld,
# OdeHashSpace,
# OdeJointGroup,
  OdeMass,
  OdeBody,
  OdeSphereGeom,
  OdeBoxGeom,
  BitMask32,
# TextNode
)
 
from Collectible import Collectible
 
class Pallo(Collectible):
    
    COLLECTIBLE_TYPE = 'PointBall'
    def __init__(self, game, color):
        self.game = game
        
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode)
 
        plight = PointLight('plight')
        plight.setPoint( Point3(0.6, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = model.attachNewNode(plight)
        model.setLight(plightNodePath)
        
        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)
        self.body.setGravityMode(False)
        #self.juttu = OdeUtil()
        
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 2)
        self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
    
 
    def PowerUpEffect(self, ship):
        ship.mass.add(self.mass)
        ship.addPower(-20)
        #print player
        print ship.SHIP_TYPE + " lost 20 power!!"
        
  # def releaseForces(self, ship):
        
       
 
 
 
 
    
 
 
 
