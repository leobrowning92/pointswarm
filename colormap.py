import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import matplotlib.cm as cm




def linear_gradient(start,finish,n=10):
    gradient=[0]*n
    gradient[0]=start
    for i in range(1,n):
        gradient[i]=[start[j]+i*(finish[j]-start[j])/float(n) for j in range(3)]
    return gradient

def polylinear_gradient(colors,spacing,n):
    """colors is a list of rgb colors, with spacing being the
    relative positions of the colors along the gradientself.
    spacings are thus sequential numbers between 0 and 1
    where the first and last items must be 0 and 1 respectively"""
    assert len(colors)==len(spacing), "every color must have a corresponding spacing"
    assert n>=2*len(colors) #soft cap on num of colors wrt n
    gradient=[]
    for i in range(len(colors)-1):
        gradient= gradient + linear_gradient(colors[i], colors[i+1], int(float(spacing[i+1])*n-float(spacing[i]*n)) )
    print(len(gradient),n)
    assert len(gradient)==n

    return gradient


if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    background_color = [1, 1, 1, 1]
    image_size = 200
    unit=1.0/image_size
    total_steps=image_size



    #foreground_colors=linear_gradient([.5,0,.5],[1,1,0],n=image_size)
    foreground_colors=polylinear_gradient([[0,0,0],[1,1,1],[0,0,0]],[0,0.2,1], n=image_size)


    def step_function(self):
        # render.clear_canvas()
        self.line([self.steps*unit,0],[self.steps*unit,1],width=unit)
        return True


    show=True
    if show:
        # These are the bits that need to be run when calling the Animation
        render = Animate(image_size, background_color, foreground_colors, step_function, interval=100, save=False, stop=total_steps)
        render.start()

    else:
        #this is what needs to be run to produce an image without animation
        image=Image_Creator(image_size, background_color, foreground_colors, step_function, stop=total_steps)
        image.create()
