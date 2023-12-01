from manim import *
import math 
import  random
class sferita(ThreeDScene): 
    def construct(self):
        
        
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.4)
        x = 2
        y = 1
        z = 1
        σ = 10
        ρ = 28
        β = 8/3
        for i in range(100):
            
            x1= 0.1 * (y-x)
            y1 = x*(0.28-z)-y
            z1 = x*y - (0.08/3)*z
            dx = σ * (y - x)         
            x += dx/10000
            dy = x * (ρ - z) - y
            y += dy/10000
            dz = x * y - β * z
            z +=  dz/10000
            
            
            self.add(Dot([x,y,z],0.05))
            x=x1
            y=y1
            z=z1
        self.wait(5)


           
          
       
       
    
