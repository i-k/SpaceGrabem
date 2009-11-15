import math
from pandac.PandaModules import (
# AmbientLight,
# DirectionalLight,
# PointLight,
  NodePath,
  Vec3,
# Vec4,
# Point3,
# Quat,
# OdeUtil,
# OdeWorld,
# OdeHashSpace,
# OdeJointGroup,
# OdeMass,
# OdeBody,
# OdeSphereGeom,
# OdeBoxGeom,
# BitMask32,
# TextNode
)
 
from GameObject import GameObject
 
class Ship(GameObject):
    #POWER = 100
        #lisaa aluksen listan alkuun
    def addShipToList(self, shipList):
        shipList[0:0] = [self]
     
    POINTS = 0
 
    #gives points
    def getPoints(self):
        return self.POINTS
 
    #Ads points
    def addPoints(self, amount):
        self.POINTS += amount
      
        
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
    
    def universalBrake(self, body):
        Velocity = self.body.getLinearVel()
        
        
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
        self.visualNode.setPos( Vec3(pos[0], pos[1], 0) )
        
