
import random

from pandac.PandaModules import (
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
  TextNode
)

from GameObject import GameObject

class Collectible(GameObject):
    #get boundaries from somewhere and put the randrange to those
    
        
    def hitShips(self, ship1, ship2):
            
        if OdeUtil.areConnected(ship1.body, self.body):
            self.setPos( Vec3(random.randrange(30), random.randrange(40), 0))
            self.PowerUpEffect(ship1)
    
            #self.body.disable()
            #self.visualNode.hide()
                
        elif OdeUtil.areConnected(ship2.body, self.body):
            self.setPos( Vec3(random.randrange(30), random.randrange(40), 0))
            self.PowerUpEffect(ship2)
    
            #self.body.disable()
            #self.visualNode.hide()
                
    def PowerUpEffect(self, ship):
        print "ZE GOGGLES!! ZEY DO NOZING!!!"