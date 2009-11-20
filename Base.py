from pandac.PandaModules import (
#  AmbientLight,
#  DirectionalLight,
#  PointLight,
  NodePath,
  Vec3,
# Vec4,
#  Point3,
#  Quat,
  OdeUtil,
# OdeWorld,
# OdeHashSpace,
# OdeJointGroup,
#  OdeMass,
#  OdeBody,
#  OdeSphereGeom,
  OdeBoxGeom,
  BitMask32,
#  TextNode
)

from StaticObject import StaticObject
#from CollectibleTypes import Restore


class Base(StaticObject):
    
    def __init__(self, game):
        self.game = game
        
        self.collGeom = OdeBoxGeom( self.game.physicsSpace, 2,2,2)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(1) )
        self.collGeom.setCollideBits( BitMask32(1) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode)
    
    def checkCollision():
        pass
    
    def osuminen(self, ship):
         if OdeUtil.collide(ship.collGeom, self.collGeom):
            if ship.hasBall():
              ship.addPoints(ship.Ball.getValue())
              ship.Ball.Restore(ship)
              print ship.SHIP_TYPE + str(ship.getPoints()) + " Points! "
              print " Base One! "