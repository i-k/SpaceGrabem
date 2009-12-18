import random
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
    #17.12.2009: collGeomInner -> collGeom, dropBall(x, y ,z, linX, linY), collectible.setPos() ja setVelocity()
    def __init__(self, game):
        self.game = game
        
        #poista se fysiikka-avaruus ja vaan tee se alue... justiinsa
        self.collGeom = OdeBoxGeom( 24,8,2 )

        
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(1) )
        self.collGeom.setCollideBits( BitMask32(1) )
        

#        self.collGeomOuter = OdeBoxGeom( self.game.physicsSpace, 28,6,2)
#        #self.collGeom.setBody(self.body)
#        self.collGeomOuter.setCategoryBits( BitMask32(1) )
#        self.collGeomOuter.setCollideBits( BitMask32(1) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('Base.egg')
        model.reparentTo(self.visualNode)

    

    def checkCollision( self, ship, collectiblelist ):
        if OdeUtil.collide(ship.collGeom, self.collGeom) and ship.hasBall():
            #if ship.hasBall():
            ship.addPoints( (ship.Ball.getValue()*2) )
            pos = self.getPos()
            ship.dropBall( x = pos[0], y = pos[1], z = 50, linX = random.randrange(-10,10), linY = (0-pos[1]) / 4 )
            print ship.SHIP_TYPE + " " +  str(ship.getPoints()) + " Points! "
            
            if (self.game.goalSfx.status() == 1):
                self.game.goalSfx.play()
            self.game.updateHUD()
            #print " Base One! "
        for collectible in collectiblelist:
            if OdeUtil.collide(collectible.collGeom, self.collGeom):
                pos = self.getPos()
                ship.addPoints(collectible.getValue())
                collectible.setPos( Vec3(pos[0], pos[1], 50))
                collectible.setVelocity(x = random.randrange(-10,10), y = (0-pos[1]) / 4)
                
                if (self.game.goalSfx.status() == 1):
                    self.game.goalSfx.play()
                self.game.updateHUD()
                print ship.SHIP_TYPE + " " + str(ship.getPoints()) + " Points! by throwing the ball"

    def addToBaseList(self, baseList):
        baseList.append(self)
        
    def setPos(self, pos, pos2):
        self.visualNode.setPos( pos )
        self.collGeom.setPosition( pos2 )

#        self.collGeomOuter.setPosition( pos )
