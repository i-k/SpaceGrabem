
import random

from pandac.PandaModules import (
#  AmbientLight,
#  DirectionalLight,
#  PointLight,
#  NodePath,
  Vec3,
#  Vec4,
#  Point3,
#  Quat,
  OdeUtil,
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

class Collectible(GameObject):
   

    
    #if-lause, kay lapi koko listan, tutkii id-numeron?
    #jos id numero = poistettavan id numero, poistetaan?
    
#    idnumber = 0
       
    def getID(self):
        return self.idnumber
    
#    def addToID(self):
#        self.idnumber += 1
        
    #lisaa collectiblen listaan
    def addToCollectibleList(self, collectibleList):
        collectibleList.append(self)
    
    def removeFromCollectibleList(self, collectibleList, id):  
        i = 0
        for collectible in collectibleList:
            if collectible.getID() == id:
                return collectibleList.pop(i)
        i += 1        
        
        
    def hitShips(self, shipList):
        
        for ship in shipList:
         #get boundaries from somewhere and put the randrange to those
            if OdeUtil.areConnected(ship.body, self.body):
            
                self.setPos( Vec3(random.randrange(30), random.randrange(40), 0))
                self.PowerUpEffect(ship)
    
            ## #self.body.disable()
            ## #self.visualNode.hide()
                
        ## elif OdeUtil.areConnected(ship2.body, self.body):
            ## self.setPos( Vec3(random.randrange(30), random.randrange(40), 0))
            ## self.PowerUpEffect(ship2)
    
            ## #self.body.disable()
            ## #self.visualNode.hide()
                
    def PowerUpEffect(self, ship):
        pass
        
        
 
      # def outOfBounds(self, x, y):
