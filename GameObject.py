
from pandac.PandaModules import (
#  NodePath,
  Vec3,
#  Point3,
)

class GameObject:
    def update(self, dt):
        self.visualNode.setHpr( self.getHpr() )
        pos = self.body.getPosition()
        self.visualNode.setPos( Vec3(pos[0] , pos[1] , pos[2]) )
    
    def setPos(self, pos):
        self.visualNode.setPos(pos)
        self.body.setPosition(pos)
        
    def setVelocity(self, x, y):
        self.body.setLinearVel(x, y, 0.0)
        
    def hideObject(self):
        self.visualNode.hide()
        self.collGeom.disable()
    
    def showObject(self):
        self.visualNode.show()
        self.collGeom.enable()
    
    def getHpr(self):
        return self.visualNode.getHpr()
    
    def getHeading(self):
        return self.getHpr().getX()
    
    def getPos(self):
        return self.body.getPosition()
        
    #    def SetBoundary(self, x_, y_):
    #        self.X = x_
    #        self.Y = y_
        
    #    def OutOfBounds(self):
    #        if self.self.X:
            