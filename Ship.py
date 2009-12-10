import math, random
from pandac.PandaModules import (
#  AmbientLight,
#  DirectionalLight,
#  PointLight,
  NodePath,
  Vec3,
#  Vec4,
#  Point3,
#  Quat,
#  OdeUtil,
#  OdeWorld,
#  OdeHashSpace,
#  OdeJointGroup,
#  OdeMass,
#  OdeBody,
#  OdeSphereGeom,
#  OdeBoxGeom,
#  BitMask32,
#  TextNode
)

from GameObject import GameObject

class Ship(GameObject):
    
        #lisaa aluksen listaan
    def addToShipList(self, shipList):
        shipList.append(self)
    
    SHIP_TYPE = None
    POWER = 100
    POINTS = 0
    Ball = None
    Ball_offset = 5.0
    
 #   hasBall = False
    
    #gives points
    def getPoints(self):
        return self.POINTS

    #Ads points
    def addPoints(self, amount):
        self.POINTS += amount


    def gotBall(self, ball):
   #     self.hasBall = True
        self.Ball = ball
        
      #  self.Ball.setbody
        
        #TODO: switch 30 with width of map and 40 with height of map (global variables??)
    def dropBall(self, x = random.randrange(30) ,y = random.randrange(40), z = 0, linX = 0, linY = 0):
   #     self.hasBall = False
        self.Ball.Restore(self)
        self.Ball.setPos( Vec3(x, y, z))
        self.Ball.setVelocity(linX, linY)
        #self.Ball.showObject()
        self.Ball = None

    def hasBall(self):
        return (self.Ball is not None)
    
    def getOffset(self):
        return self.Ball_offset
        
    def getShipType(self):
        return self.SHIP_TYPE
        
    def thrustOn(self):
        self.thrust = True
            
    def thrustOff(self):
        self.thrust = False
    
    def thrustLeftOn(self):
        self.thrustLeft = True
                    
    def thrustLeftOff(self):
        self.thrustLeft = False
    
    def thrustRightOn(self):
        self.thrustRight = True
            
    def thrustRightOff(self):
        self.thrustRight = False
    
    def thrustBackOn(self):
        self.thrustBack = True
            
    def thrustBackOff(self):
        self.thrustBack = False
    
    def releaseBall(self):
        #releases ball behind the ship
        if self.hasBall():
            linearVector = self.body.getLinearVel()
            heading = self.getHpr()
            position = self.getPos()
            x = position[0] + (math.sin(math.radians(heading[0])) * self.getOffset())
            y = position[1] + (-math.cos(math.radians(heading[0])) * self.getOffset())
            
#ihme miten auttaa kun koittaa hieman katsoa mita lukuja tuolta tulee
#            print str(heading[0]) + " heading x of ship"
#            print str(heading[1]) + " heading y of ship"
#            print str(x) + " x of ball test debug joo"
#            print str(y) + " y something"
            
            self.dropBall( x, y, linX = linearVector[0], linY = linearVector[1] )
            
#    def universalBrake(self, body):
#        Velocity = self.body.getLinearVel() 
        
        
    def rotate(self, rotate):
        self.rotation += rotate
            
    def setRotation(self, amount):
        self.rotation = amount
    
    def setRotationSmooth(self, speed, amount):
        if self.rotation > amount:
            self.rotation -= speed
        if self.rotation < amount:
            self.rotation += speed
    
    def setPower(self, amount):
        self.POWER = amount
    
    def addPower(self, amount):
        self.POWER += amount
            
    def applyForces(self):
        if self.thrust:
            heading = self.getHeading()
            self.body.addForce(
                -math.sin( math.radians(heading) ) * self.POWER,
                math.cos( math.radians(heading) ) * self.POWER,
                0
            )
            
    def update(self, dt):
        self.visualNode.setHpr( self.getHpr() + Vec3(self.rotation * 2.5, 0, 0) )
        pos = self.body.getPosition()
        self.setPos( Vec3(pos[0], pos[1], 0) )
        