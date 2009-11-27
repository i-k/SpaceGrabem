from StaticObject import bigWall

from pandac.PandaModules import (
  Vec3
)


class Map:

    wallList = None

        

    def makeBoundaryWalls(self, MapX = 150.0, MapY = 150.0, WallLength = 50.0 ):
        WALLS = range(1, int(2*((MapX / WallLength) + 1)))
        for Wall in WALLS:
            BigWall1 = bigWall(self)
            BigWall1.setPos( Vec3(-MapX + (WallLength*Wall)-(WallLength / 2) , -MapY, 0) )
            BigWall2 = bigWall(self)
            BigWall2.setPos( Vec3(-MapX + (WallLength*Wall)-(WallLength / 2) , +MapY, 0) )
            BigWall3 = bigWall(self)
            BigWall3.setRotation( 90 )
            BigWall3.setPos( Vec3(-MapX , -MapY + (WallLength*Wall)-(WallLength / 2), 0) )
            BigWall4 = bigWall(self)
            BigWall4.setRotation( 90 )
            BigWall4.setPos( Vec3(+MapX , -MapY + (WallLength*Wall)-(WallLength / 2), 0) )
            #self.wallList.append(BigWall1)
            #self.wallList.append(BigWall2)
            #self.wallList.append(BigWall3)