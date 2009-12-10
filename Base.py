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
        
        #poista se fysiikka-avaruus ja vaan tee se alue... justiinsa
        self.collGeomInner = OdeBoxGeom( 24,8,2 )
        self.collGeomInner = OdeBoxGeom( self.game.physicsSpace, 24,8,2)
        
        #self.collGeom.setBody(self.body)
        self.collGeomInner.setCategoryBits( BitMask32(1) )
        self.collGeomInner.setCollideBits( BitMask32(1) )
        

#        self.collGeomOuter = OdeBoxGeom( self.game.physicsSpace, 28,6,2)
#        #self.collGeom.setBody(self.body)
#        self.collGeomOuter.setCategoryBits( BitMask32(1) )
#        self.collGeomOuter.setCollideBits( BitMask32(1) )

        self.collGeomOuter = OdeBoxGeom( self.game.physicsSpace, 28,6,2)
        #self.collGeom.setBody(self.body)
        self.collGeomOuter.setCategoryBits( BitMask32(1) )
        self.collGeomOuter.setCollideBits( BitMask32(1) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('Base.egg')
        model.reparentTo(self.visualNode)

    

    def checkCollision( self, ship):
         if OdeUtil.collide(ship.collGeom, self.collGeomInner) and ship.hasBall():
            #if ship.hasBall():
            ship.addPoints(ship.Ball.getValue())
            ship.dropBall( z = 300 )
            print ship.SHIP_TYPE + " " +  str(ship.getPoints()) + " Points! "
            #print " Base One! "
            
    def addToBaseList(self, baseList):
        baseList.append(self)
        
    def setPos(self, pos):
        self.visualNode.setPos( pos )
        self.collGeomInner.setPosition( pos )

 #       self.collGeomOuter.setPosition( pos )
