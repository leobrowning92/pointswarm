import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import matplotlib.cm as cm


def random_rgb_color(alpha=1):
    return [np.random.uniform(0,1),np.random.uniform(0,1), np.random.uniform(0,1),alpha]


def linear_gradient(start,finish,n=10,alpha=1):
    gradient=[0]*n
    gradient[0]=start
    for i in range(1,n):
        gradient[i]=[start[j]+i*(finish[j]-start[j])/float(n) for j in range(3)]+[alpha]
    return gradient

def polylinear_gradient(colors,spacing,total_steps,alpha=1):
    """colors is a list of rgb colors, with spacing being the
    relative positions of the colors along the gradientself.
    spacings are thus sequential numbers between 0 and 1
    where the first and last items must be 0 and 1 respectively"""
    assert len(colors)==len(spacing), "every color must have a corresponding spacing"
    assert total_steps>=2*len(colors) #soft cap on num of colors wrt n
    gradient=[]
    for i in range(len(colors)-1):
        gradient= gradient + linear_gradient(colors[i], colors[i+1], spacing[i+1] -spacing[i],alpha=alpha )
    assert len(gradient)==total_steps

    return gradient

def hex_to_rgb(hex):
    return [int(hex[i:i+2]) for i in range(1,6,2)]

def random_colormap(number_of_colors,total_steps, even=True,v=True,alpha=1):
    colors=[]
    spacing=[0]
    for i in range(number_of_colors):
        colors.append(random_rgb_color(alpha=alpha))


    if even:
        spacing=np.linspace(0,total_steps,num=number_of_colors,dtype=int)
    else:
        for i in range(number_of_colors-2):
            spacing.append(np.random.uniform(0.01,0.99))
        spacing.append(1)
    if v:
        print("colors:")
        for i in colors:
            print(*i)
        print("spacing:\n", *sorted(spacing))
    return polylinear_gradient(colors,sorted(spacing),total_steps,alpha=alpha)

if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    background_color = [1, 1, 1, 1]
    image_size = [200,200]
    unit=1.0/max(image_size)
    total_steps=max(image_size)



    #foreground_colors=linear_gradient([.5,0,.5],[1,1,0],n=image_size)
    #foreground_colors=random_colormap(3,total_steps,even=False)
    colors=np.genfromtxt(fname='sourceimages/IMG_9308_kmean6.dat',skip_header=1,delimiter=',')
    foreground_colors=polylinear_gradient(colors,np.linspace(0,total_steps,num=len(colors),dtype=int) ,total_steps)

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
