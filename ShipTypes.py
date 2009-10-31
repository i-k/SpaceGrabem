import math

from pandac.PandaModules import (
  AmbientLight,
  DirectionalLight,
  PointLight,
  NodePath,
  Vec3,
  Vec4,
  Point3,
  Quat,
  OdeUtil,
  OdeWorld,
  OdeHashSpace,
  OdeJointGroup,
  OdeMass,
  OdeBody,
  OdeSphereGeom,
  OdeBoxGeom,
  BitMask32,
  TextNode
)

from Ship import Ship

class Ship_1(Ship):
    
    POWER = 100
    SHIP_TYPE = "UFO"
    
    def __init__(self, game, color):
        #self.POWER = 100
        self.game = game
        
        self.thrust = False
        self.thrustLeft = False
        self.thrustRight = False
        self.thrustBack = False
        self.rotation = 0

        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)

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
        model.setLight(plightNodePath)
        
 # setMoreKeys in ship class = BAD IDEA
    #def setMoreKeys(self):
     #   base.accept('arrow_down', self.thrustBackOn)
      #  base.accept('arrow_down-up', self.thrustBackOff) 
      

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
    
    ROTATING_SPEED = 1
    MAX_ROTATE_SPEED = 3.0
    SHIP_TYPE = "RAKETTI"
    
    def __init__(self, game, color):

        self.POWER = 100
        self.game = game
        
        self.thrust = False
        self.thrustLeft = False
        self.thrustRight = False
        self.thrustBack = False
        self.rotation = 0

        self.body = OdeBody(game.physicsWorld)
        self.mass = OdeMass()
        self.mass.setBox(10,1,1,1)
        self.body.setMass(self.mass)

        #odespheregeom(... , size of hitbox sphere)
        self.collGeom = OdeSphereGeom( self.game.physicsSpace, 2)
        self.collGeom.setBody(self.body)
        self.collGeom.setCategoryBits( BitMask32(0xffffffff) )
        self.collGeom.setCollideBits( BitMask32(0xffffffff) )
        
        self.visualNode = NodePath('Visual node')
        self.visualNode.reparentTo(render)
        model = loader.loadModel('testipalikka.egg')
        model.reparentTo(self.visualNode)
        
        plight = PointLight('plight')
        plight.setPoint( Point3(0.6, 0, 5) )
        plight.setColor( color )
        plight.setAttenuation( Vec3(0.5, 0.01, 0.01) )
        plightNodePath = model.attachNewNode(plight)
        model.setLight(plightNodePath)



    
    
    def rotating(self):
        if self.thrustLeft:
            self.setRotation(self.ROTATING_SPEED)
        if self.thrustRight:
            self.setRotation(-(self.ROTATING_SPEED))
        if not self.thrustRight and not self.thrustLeft:
            self.setRotation(0)


    def applyForces(self):
        if self.thrust:
            heading = self.getHeading()
            #addForce (x, y, z)
            self.body.addForce(
              -math.sin( math.radians(heading) ) * self.POWER,
               math.cos( math.radians(heading) ) * self.POWER,
              0
            )
# uncomment for backwards thrust (eli siis pakki)
#        if self.thrustBack:
#            heading = self.getHeading()
#            self.body.addForce(
#               math.sin( math.radians(heading) ) * self.POWER,
#              -math.cos( math.radians(heading) ) * self.POWER,
#              0
#            )
        self.rotating()


