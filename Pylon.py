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
    
    def __init__(self, game, power = 50.0, range = 30):
        self.game = game
        self.POWER = power
        self.Active = False
        self.RANGE = range
        
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 3)
        #self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
        
        self.triggerGeom = OdeSphereGeom( range ) 
        self.triggerGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.triggerGeom.setCollideBits( BitMask32(0xffffffff) )
                
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        self.model = loader.loadModel('AbsorbingPylon.egg')
        self.model.setScale(1.5)
        self.model.reparentTo(self.visualNode)
        
        pow = self.getPower()*5
        maxPow = self.game.MAX_PYLON_POWER
        if (pow > 0):
            self.offColor = Vec4(pow/maxPow, 0.0, 0.0, 0.0)
            self.onColor = Vec4(0.0, pow/maxPow, 0.0, 0.0)

        if (pow <= 0):
            self.offColor = Vec4(0.0, 0.0, -pow/maxPow, 0.0)
            self.onColor = Vec4(0.0, -pow/maxPow, 0.0, 0.0)
            
        self.setColor( self.offColor )
            
    def setPos(self, pos):
        self.visualNode.setPos( pos )
        self.collGeom.setPosition( pos )
        self.triggerGeom.setPosition( pos )
        
    def addToPylonList(self, pylonList):
        pylonList.append(self)
        
    def getPower(self):
        return self.POWER
        
    def getRange(self):
        return self.RANGE
        
        
    def setColor(self, color):
        plight = PointLight('plight4')
        plight.setPoint( Point3(0.6, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        self.plight = plight
        self.plightNodePath = self.model.attachNewNode(self.plight)
        self.model.setLight(self.plightNodePath)

    def setActive(self, active, ship):
        if active == self.Active:
            return
        if active:
            self.whoActivated = ship
            self.plight.setColor(self.onColor)
            self.Active = active
        else:
            if ship == self.whoActivated:
                self.plight.setColor(self.offColor)
                self.Active = active
        
    def isActive(self):
        return self.Active
        
    #checks when ship gets inside the trigger zone of this pylon
    def insideTrigger(self, ship):
        if OdeUtil.collide(self.triggerGeom, ship.collGeom):
           # self.setActiveOn()
            #print str(ship.getShipType())
            self.setActive(True, ship)
            self.usingTheForce( ship )
           # print "moo"
        else:
            #self.setActiveOff()
            #print "muu"
            self.setActive(False, ship)
            
    #applies force to ship relative to the position of the pylon
    #while ship is inside trigger zone
    def usingTheForce(self, ship):
        #if (self.isActive()):
            #algoritmi ei toimi viela optimaalisesti 
            pylonpos = self.getPos()
            shippos = ship.getPos()
            relativepos = [ (shippos[0] - pylonpos[0])  , (shippos[1] - pylonpos[1]) ] 
#            if (shippos[0] - pylonpos[0]) < 0:
#                relativepos = []

            ship.body.addForce( relativepos[0] * self.POWER, relativepos[1] * self.POWER, 0  )

    
#    #checks if collision happens with one ship 
#    #quite useless, but leaving it anyway
#    def checkCollision(self, ship):
#         if OdeUtil.collide(ship.collGeom, self.collGeom) and ship.hasBall():
#            #ship.Ball.Restore(ship)
#            ship.dropBall( z = 300 )
#            print str(ship.getShipType()) + " lost its balls! ONOES!!"

    
    #checks if collision happens with a ship in the list of ships
    #also checks if ship is inside the range of the pylon's power
    def checkCollisionList(self, shipList):
        for ship in shipList:
            self.insideTrigger( ship )
            #self.usingTheForce( ship )
            if OdeUtil.collide(ship.collGeom, self.collGeom) and ship.hasBall():
                #ship.Ball.Restore(ship)
                if (self.game.collision2Sfx.status() == 1):
                    self.game.collision2Sfx.play()
                pos = ship.getPos()
                ship.dropBall(x = pos[0], y = pos[1], z = 30, linX = ( (0-pos[0])/7 ), linY = ( (0-pos[1])/7 ), linZ = 2)
                print str(ship.getShipType()) + " lost its balls! NOOOO!"
