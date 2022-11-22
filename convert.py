from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials
import numpy as np

def isEmpty(array):
    for i in array:
        for j in i:
            if j==1:
                return False
    return True




def makeVoxel(top,front,side,name):
    print(top,front,side)

    voxel=np.ones((10,10,10),dtype=bool)
    

    #top part
    if(not isEmpty(top)):
        for i in range(10):
            for j in range(10):
                if top[i][j]==0:
                    for k in range(10):
                        voxel[i,j,k]=False
                    
    
    #front part
    if(not isEmpty(front)):
        for i in range(10):
            for j in range(10):
                if front[i][j]==0:
                    for k in range(10):
                        voxel[i,k,j]=False
                

    #side part
    if(not isEmpty(side)):
        for i in range(10):
            for j in range(10):
                if side[i][j]==0:
                    for k in range(10):
                        voxel[k,i,j]=False
                  


    print(voxel)


    




    model = VoxelModel(voxel, generateMaterials(4))  #4 is aluminium.
    mesh = Mesh.fromVoxelModel(model)
    mesh.export(name+'.stl')