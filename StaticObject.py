from GameObject import GameObject

from pandac.PandaModules import (
OdeBoxGeom,
NodePath,
BitMask32,
OdeUtil
)

class bigWall(GameObject):
#TODO: rotate method (maybe a staticobject class too)   

    
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
        
        
    def setPos(self, pos):
        self.visualNode.setPos( pos )
        self.collGeom.setPosition( pos )
        
        
        
    def osuminen(self, ship1):
         if OdeUtil.collide(ship1.collGeom, self.collGeom):
 
            print "sdfgfdhgdfhxfhdhghcfh"
            print "ship1 xdfhgxdgxdgfbcdll!!"
    
class smallWall(GameObject):
    

        
         
    def __init__(self, game):
        
        self.collGeom = OdeBoxGeom( self.game.physicsSpace, 10, 2, 2)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0x000000ff) )
        self.collGeom.setCollideBits( BitMask32(0x000000ff) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode)
        
    def setPos(self, pos):
        self.visualNode.setPos( pos )
        self.collGeom.setPosition( pos )  