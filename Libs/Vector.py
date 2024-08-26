'''
    Vector Libary

    Made by Daan Sijnja
    
    For usage of Vector2 and Vector3

'''
import math

class Vector2:
    '''
        Vector2 class to make the caculatiions easier 

        Functions:
            Vector2(x,y,bx=0,by=0,color=[255,0,0])
            Translate(_vector)
            Rotate(_angle)
    '''

    def __init__(self,x,y):
        '''
            @param x : int | the x endpoint of the vector
            @param y : int | the y endpoint of the vector  
        '''
        self.value = [x,y]

    def Translate(self,_vector):
        '''
            Translate the vector by an other vector this is not how a translation matrix works but its simplified 
            for this purpose

            @param _vector : Vector2 | the vector with which should be translated by

            @returns Vector2 : creates an new vector as output because we want to keep the orignal values of the Vector2 in the Pendulum class
        '''
        p1 = [
              self.value[0] + _vector.value[0], 
              self.value[1] + _vector.value[1]
            ]

        return Vector2(p1[0],p1[1])

    def Rotate(self,_angle):
        '''
            Rotates the vector by the given angle | in this code the rotation matrix is written out in code

            @param _angle : int or float | the vector will be rotated by this angle

            @returns Vector2 : creates an new vector as output because we want to keep the orignal values of the Vector2 in the Pendulum class
        '''
        p1 = self.value[:] 
        new_p1 = [
                math.cos(math.radians(_angle))*p1[0] - math.sin(math.radians(_angle))*p1[1],
                math.sin(math.radians(_angle))*p1[0] + math.cos(math.radians(_angle))*p1[1]
                ]
        return Vector2(new_p1[0],new_p1[1])
    
    
