from pandac.PandaModules import (
PointLight,
Point3,
Vec3,
Vec4,
OdeSphereGeom,
NodePath,
BitMask32,
OdeUtil
)

from StaticObject import StaticObject

class Pylon(StaticObject):
    
    
    
    def __init__(self, game, power = 10):
        self.game = game
        self.POWER = power
        self.Active = False
        
        
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 3)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        self.model = loader.loadModel('testipalikka.egg')
        self.model.reparentTo(self.visualNode)
        
        #TODO: trigger geom
        #self.effectGeom = OdeSphereGeom(  )
        
        if (self.getPower() > 0):
            self.setColor( Vec4(1.0, 0.0, 0.0, 0.0) )
        if (self.getPower() <= 0):
            self.setColor( Vec4(0.0, 0.0, 1.0, 0.0) )
            
        
    def addToPylonList(self, pylonList):
        pylonList.append(self)
        
    def getPower(self):
        return self.POWER
        
    def setColor(self, color):
        plight = PointLight('plight')
        plight.setPoint( Point3(0.6, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = self.model.attachNewNode(plight)
        self.model.setLight(plightNodePath)
        
    def setActiveOn(self):
        self.Active = True
        
    def setActiveOff(self):
        self.Active = False
        
    def isActive(self):
        return self.Active
        
    #checks when ship gets inside the trigger zone of this pylon
    def insideTrigger(self, ship):
        pass
#        if OdeUtil.collide(ship.collGeom, self.effectGeom)
#            self.setActiveOn()        
    
    
    
    #applies force to ship relative to the position of the pylon
    #while ship is inside trigger zone
    def usingTheForce(self, ship):
        if (self.isActive()):
            pass
        
    
    #checks if collision happens with one ship 
    #quite useless, but leaving it anyway
    def checkCollision(self, ship):
         if OdeUtil.collide(ship.collGeom, self.collGeom) and ship.hasBall():
            #ship.Ball.Restore(ship)
            ship.dropBall()
            print str(ship.getShipType()) + " lost its balls! ONOES!!"
    
    #checks if collision happens with a ship in the list of ships
    def checkCollisionList(self, shipList):
        for ship in shipList:
            if OdeUtil.collide(ship.collGeom, self.collGeom) and ship.hasBall():
                #ship.Ball.Restore(ship)
                ship.dropBall()
                print str(ship.getShipType()) + " lost its balls! NOOOO!"
