from GameObject import GameObject

from pandac.PandaModules import (
Vec3,
OdeBoxGeom,
NodePath,
BitMask32,
OdeUtil
)

class StaticObject(GameObject):

    def setPos(self, pos):
        self.visualNode.setPos( pos )
        self.collGeom.setPosition( pos )

    #rotate in degrees counterclockwise
    def setRotation(self, rotate):
        self.rotation = rotate
        self.update()
               
    #experiment so the model turns as much as the hitbox
    def update(self):
        self.visualNode.setHpr( Vec3(self.rotation, 0, 0) )
        pos = self.collGeom.getRotation()
        self.collGeom.setRotation( pos.rotateMat(self.rotation) )
   



class bigWall(StaticObject):


    
    def __init__(self, game):
        self.game = game
        
        
        self.collGeom = OdeBoxGeom( self.game.physicsSpace, 50, 2, 2)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0x000000ff) )#ffffffff) )
        self.collGeom.setCollideBits( BitMask32(0x000000ff) )
        
        #remember to make wall model with "50" length... no idea 50 what, though
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode) 
        
        
   
        
        
    def osuminen(self, ship1):
         if OdeUtil.collide(ship1.collGeom, self.collGeom):
 
            print "sdfgfdhgdfhxfhdhghcfh"
            print "ship1 xdfhgxdgxdgfbcdll!!"
    
class smallWall(StaticObject):
    

        
         
    def __init__(self, game):
        
        self.collGeom = OdeBoxGeom( self.game.physicsSpace, 10, 2, 2)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0x000000ff) )
        self.collGeom.setCollideBits( BitMask32(0x000000ff) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode)
        