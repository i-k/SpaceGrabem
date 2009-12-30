import math

from pandac.PandaModules import (
  PointLight,
  NodePath,
  Vec3,
  Vec4,
  Point3,
#  Quat,
#  OdeUtil,
#  OdeWorld,
#  OdeHashSpace,
#  OdeJointGroup,
  OdeMass,
  OdeBody,
  OdeSphereGeom,
  OdeCylinderGeom,
  OdeTriMeshGeom,
  OdeTriMeshData,
#  OdeBoxGeom,
  BitMask32,
#  TextNode
)

from Ship import Ship

class Ship_1(Ship):
    
    def __init__(self, game, color):
        self.POWER = 1000
        self.game = game
        self.SHIP_TYPE = "UFO"
        self.Ball_offset = 10.0
     #   self.hasBall = False
        self.thrust = False
        self.thrustLeft = False
        self.thrustRight = False
        self.thrustBack = False
        self.rotation = 0

        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)
        #self.body.setGravityMode(False)

        #odespheregeom(... , size of hitbox sphere)
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 5)
        self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('lautanen2.egg')
        model.reparentTo(self.visualNode)
        
        plight = PointLight('plight')
        plight.setPoint( Point3(0.6, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = model.attachNewNode(plight)
        self.visualNode.setLight(plightNodePath)
        game.map.agplate.visualNode.setLight(plightNodePath)
        
 # setMoreKeys in ship class = BAD IDEA
    #def setMoreKeys(self):
     #   base.accept('arrow_down', self.thrustBackOn)
      #  base.accept('arrow_down-up', self.thrustBackOff) 
      
    #Hiukan turhan monimutkainen perhaps? Antaa olla, ei jaksa
    def applyForces(self):
        if self.thrust:
            heading = self.getHeading()
            self.body.addForce(
              -math.sin( math.radians(heading) ) * self.POWER,
               math.cos( math.radians(heading) ) * self.POWER,
               0
            )
        if self.thrustLeft:
            heading = self.getHeading()
            self.body.addForce(
              -math.sin( math.radians(heading) + math.pi/2 ) * self.POWER,
               math.cos( math.radians(heading) + math.pi/2 ) * self.POWER,
               0
            )
        if self.thrustRight:
            heading = self.getHeading()
            self.body.addForce(
              -math.sin( math.radians(heading) - math.pi/2 ) * self.POWER,
               math.cos( math.radians(heading) - math.pi/2 ) * self.POWER,
               0
            )
        if self.thrustBack:
            heading = self.getHeading()
            self.body.addForce(
              -math.sin( math.radians(heading) + math.pi ) * self.POWER,
               math.cos( math.radians(heading) + math.pi ) * self.POWER,
               0
            )


class Ship_2(Ship):
    
    ROTATING_SPEED = 2
    MAX_ROTATE_SPEED = 3.0
   
    
    def __init__(self, game, color):

        self.POWER = 1000
        self.game = game
        self.SHIP_TYPE = "RAKETTI"
        self.Ball_offset = 10.0
     #   self.hasBall = False
        self.thrust = False
        self.thrustLeft = False
        self.thrustRight = False
        self.thrustBack = False
        self.rotation = 0

        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)
     
        self.collGeom = OdeCylinderGeom( self.game.physicsSpace, 3, 10)
        self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
    
        self.collGeom2 = OdeSphereGeom( self.game.physicsSpace, 4)
        self.collGeom2.setBody(self.body)
        self.collGeom2.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom2.setCollideBits( BitMask32(0xffffffff) )
        
        pos1 = self.body.getPosition()
#        pos = [ (pos1[0] - 10), (pos1[1] + 30), pos1[2] ]
        self.collGeom2.setPosition( (pos1[0] - 10), (pos1[1] + 30), pos1[2] )
        
        self.collGeom3 = OdeSphereGeom( self.game.physicsSpace, 4)
        self.collGeom3.setBody(self.body)
        self.collGeom3.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom3.setCollideBits( BitMask32(0xffffffff) )
        
       
        self.collGeom3.setPosition( (pos1[0] + 10), (pos1[1] + 30), pos1[2] )

        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('spaceship.egg')
#        model.setH(180)
#        model.setY(15)
        model.reparentTo(self.visualNode)
        self.visualNode.setScale(0.4)
        plight = PointLight('plight2')
        plight.setPoint( Point3(0, 8, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = model.attachNewNode(plight)
        self.visualNode.setLight(plightNodePath)
        game.map.agplate.visualNode.setLight(plightNodePath)

        aBurnerOuter = PointLight('aBurnerOuter')
        aBurnerOuter.setPoint( Point3(0, -20, 0) )
        aBurnerOuter.setColor( Vec4(1,0,0,0) )
        aBurnerOuter.setAttenuation( Vec3(1, 1, 1) )
        outerNode = model.attachNewNode(aBurnerOuter)
        self.visualNode.setLight(outerNode)
        game.map.agplate.visualNode.setLight(outerNode)
        game.map.walls.setLight(outerNode)
        
        aBurnerInner = PointLight('aBurnerInner')
        aBurnerInner.setPoint( Point3(0, -25, 0) )
        aBurnerInner.setColor( Vec4(1,1,0,0) )
        aBurnerInner.setAttenuation( Vec3(1, 1, 1) )
        innerNode = model.attachNewNode(aBurnerInner)
        self.visualNode.setLight(innerNode)
        game.map.agplate.visualNode.setLight(innerNode)
        game.map.walls.setLight(innerNode)
        
        self.afterBurner = [aBurnerInner, aBurnerOuter]
        self.afterBurnerOn = False
    
    def rotating(self):
        if self.thrustLeft:
            self.setRotation(self.ROTATING_SPEED)
        if self.thrustRight:
            self.setRotation(-(self.ROTATING_SPEED))
        if not self.thrustRight and not self.thrustLeft:
            self.setRotation(0)


    def applyForces(self):
        if self.thrust:
            self.setAfterBurner(True)
            heading = self.getHeading()
            #addForce (x, y, z)
            self.body.addForce(
              -math.sin( math.radians(heading) ) * self.POWER,
               math.cos( math.radians(heading) ) * self.POWER,
              0
            )
        else:
            self.setAfterBurner(False)
# uncomment for backwards thrust (eli siis pakki)
#        if self.thrustBack:
#            heading = self.getHeading()
#            self.body.addForce(
#               math.sin( math.radians(heading) ) * self.POWER,
#               -math.cos( math.radians(heading) ) * self.POWER,
#               0
#                  
#               )
        self.rotating()


    def setAfterBurner(self, on):
        if self.afterBurnerOn == on:
            return
        if on:
            self.afterBurner[0].setAttenuation( Vec3(0.02, 0.02, 0.02) )
            self.afterBurner[1].setAttenuation( Vec3(0.01, 0.01, 0.01) )
        else:
            self.afterBurner[0].setAttenuation( Vec3(1, 1, 1) )
            self.afterBurner[1].setAttenuation( Vec3(1, 1, 1) )
        self.afterBurnerOn = on
