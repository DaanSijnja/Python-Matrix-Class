'''
    Plotter Libary

    Made by Daan Sijnja
    Used for making a plot of different graphs, lines or points

    Uses OpenCV (cv2) as base for showing the plot

'''
import cv2 as cv

class CoordinateSystem:
    def __init__(self,_scale,_midpoint,_flipYAxis = False, _color = [255,255,255]):
        '''
            @param _scale : int[2] | how many pixels one unit is
            @param _midpoint : float[2] | the midpoint of the coordinate system

            Optional:
            @param _flipYAxis : bool | if the y axis should be inverted | default : False
            @param _color : int[3] | RGB color of the drawn coordinate system | default : [255,255,255] (white)
        '''
        self.scale = _scale
        self.midpoint = _midpoint
        self.flipYAxis = _flipYAxis
        self.color = _color

    def Recalculate(self,_point,planeSize):
        '''
            This fuction recalulates the point to scale with the coordinate system
            @param _point : float[2] | a point that needs to be recalculated
        '''
        _p = _point[:]
        
        _p[0] = int(planeSize[0]*self.midpoint[0]) + int(_p[0]*self.scale[0])
        _p[1] = int(planeSize[1]*self.midpoint[1]) + int(_p[1]*self.scale[1] * (1 if self.flipYAxis else -1))

        return _p
    
    def DrawCoordinateSystem(self,_img,_labels = ["x","y"], _unitsShown = True):
        '''
            This fuction draws the coordinate system on an given image
            @param _img : int[x][y][3] | An matrix with size x by y by 3 from the opencv libary

            Optional:
            @param _labels : string[2] | labels for the x and y axis | default : ["x","y"]
            @param _unitsShown : bool | if the units should be shown or not | default : True

            Return:
            @retun _img : int[x][y][3] | returns the image with the coord system plotted on it.
        '''
        y, x, _ = _img.shape                                                                        # Get the x and y size of the given image

        p1 = []                                                                                     # Initalize p1 as an empty array
        p2 = []                                                                                     # Initalize p2 as an empty array

        #y axis line
        _x = int(self.midpoint[0]*x)                                                                # Caclulates the x value of the y-axis line
        p1 = [_x,0]                                                                                 # Sets p1 to x of the y-axis line and makes the y component 0
        p2 = [_x,y]                                                                                 # Sets p2 to x of the y-axis line and makes the y component the max image y
        cv.line(_img,p1,p2,self.color,1)                                                            # Draws a line with openCV with the points p1 and p2
        
        p3 = p2[:]
        p3[0] += 10 
        if(self.flipYAxis):
            p3[1] -= 10  
        else:
            p3[1] = 10 
        cv.putText(_img,_labels[1],p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)

        #y axis lines positive side
        _ylines = (y - y*self.midpoint[1]) // self.scale[1]                                         # Caclulates how many whole units there on the positve y-axis
        for i in range(1,int(_ylines+1)):                                                           # +1 because its acualy caculates how many unit spaces there are
            _yPos = y*self.midpoint[1] + self.scale[1]*i                                            # caculates the y pos of the unit line

            p1 = [ _x , int(_yPos)]                                                                 # 
            p2 = [ _x - 10 ,int(_yPos)]                                                             # -10 is the unit line length
            cv.line(_img,p1,p2,self.color,1)                                                        # Draw the line with the given points p1 and p2
            
            if(_unitsShown):
                p3 = p2[:]                                                                          # Copy p2 to p3
                p3[0] = _x - 20  if self.flipYAxis else _x - 30                                     # add some extra distance for the text
                p3[1] = int(_yPos) + 15 
                cv.putText(_img,f'{i if self.flipYAxis else -i}',p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)          # Draw the text to the given position

        #y axis lines negative side
        _ylines = (y*self.midpoint[1]) // self.scale[1]                                             
        for i in range(1,int(_ylines+1)):                                                           
            _yPos = y*self.midpoint[1] + self.scale[1]*(-i)                                         

            p1 = [ _x , int(_yPos)]                                                                 
            p2 = [ _x - 10 ,int(_yPos)]                                                             
            cv.line(_img,p1,p2,self.color,1)                                                        

            if(_unitsShown):
                p3 = p2[:]                                                                          # Copy p2 to p3
                p3[0] = _x - 30 if self.flipYAxis else _x - 20                                      # add some extra distance for the text
                p3[1] = int(_yPos) + 15  
                cv.putText(_img,f'{-i if self.flipYAxis else i}',p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)         # Draw the text to the given position

        #x axis line
        _y = int(self.midpoint[1]*y)                                                                # Caclulates the x value of the y-axis line
        p1 = [0,_y]                                                                                 # Sets p1 to y of the x-axis line and makes the x component 0
        p2 = [x,_y]                                                                                 # Sets p2 to y of the x-axis line and makes the x component the max image x
        cv.line(_img,p1,p2,self.color,1)                                                            # Draws a line with openCV with the points p1 and p2

        p3 = p2[:]
        p3[0] -= 15 
        p3[1] -= 10
        cv.putText(_img,_labels[0],p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)

        #x as line + side
        _xlines = (x - x*self.midpoint[0]) // self.scale[0]                                         
        for i in range(1,int(_xlines+1)):                                                           
            _xPos = x*self.midpoint[0] + self.scale[0]*i                                            

            p1 = [int(_xPos), _y]                                                                   
            p2 = [int(_xPos), _y+10]                                                                
            cv.line(_img,p1,p2,self.color,1)                                                        

            if(_unitsShown):
                p3 = p2[:]                                                                          # Copy p2 to p3
                p3[0] = int(_xPos) + 5                                                              # add some extra distance for the text
                p3[1] =  _y + 20
                cv.putText(_img,f'{i}',p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)      # Draw the text to the given position

        #x as line - side
        _xlines = (x*self.midpoint[0]) // self.scale[0]                                             
        for i in range(1,int(_xlines+1)):                                                           
            _xPos = x*self.midpoint[0] + self.scale[0]*(-i)                                         

            p1 = [int(_xPos), _y]                                                                   
            p2 = [int(_xPos), _y+10]                                                                
            cv.line(_img,p1,p2,self.color,1)                                                        
            if(_unitsShown):
                p3 = p2[:]                                                                          # Copy p2 to p3
                p3[0] = int(_xPos) + 5                                                              # add some extra distance for the text
                p3[1] =  _y + 20  
                cv.putText(_img,f'{-i}',p3,cv.FONT_HERSHEY_SIMPLEX,0.5,self.color,1,cv.LINE_AA)     # Draw the text to the given position

        return _img        

class Plotter:
    def __init__(self) -> None:
        pass
    
    def DrawLine(self,_img,_line,_color,_thickness = 2,_coordSystem=CoordinateSystem([1,1],[0,0],_flipYAxis=True)):
        '''
            This method is used to draw a line with a given Coordinate System
        
            @param _img : openCV image | the image where the line should be drawn on
            @param _line : float[2][2] | a line consisting of 2 points : float[2]
            @param _color : int[3] | the color BGR which the line should have
            
            Optional:
            @param _thickness : int | the thickness of the line | default = 2 
            @param _coordSystem : CoordinateSystem | the Coordinate System where the line should be drawn in
        
        '''
        h, w, _ = _img.shape                                                                        # Get the size of the image

        p1 = _coordSystem.Recalculate(_line[0][:],[w,h])                                            # Recalculate the point to the image
        p2 = _coordSystem.Recalculate(_line[1][:],[w,h])                                            # Recalculate the point to the image

        cv.line(_img,p1,p2,_color,_thickness)                                                       # openCV draw the line

    def DrawPoint(self,_img,_point,_color,_size= 5,_coordSystem=CoordinateSystem([1,1],[0,0],_flipYAxis=True)):
        '''
            This method is used to draw a line with a given Coordinate System
        
            @param _img : openCV image | the image where the line should be drawn on
            @param _point : float[2] | a point 
            @param _color : int[3] | the color BGR which the line should have
            
            Optional:
            @param _size : int | the size of the point | default = 5
            @param _coordSystem : CoordinateSystem | the Coordinate System where the point should be drawn in
        
        '''
        h, w, _ = _img.shape                                                                        # Get the size of the image

        p = _coordSystem.Recalculate(_point[:],[w,h])                                               # Recalculate the point to the image

        cv.circle(_img,p,_size,_color,thickness=-1)                                                 # openCV draw the point

    def Plot(self,_canvas):
        '''
            Shows the given canvas

            @param _canvas : OpenCV image | the image that needs to be shown

            @return : bool | returns 0 when the esc key is hit for quiting the application

        '''
        cv.imshow('Plotter',_canvas)                                                                # OpenCV for showing the image

        k = cv.waitKey(30) & 0xff                                                                   #check for esc-key
        if (k == 27):                                                                               
            return 0
        
        return 1


       
        

        