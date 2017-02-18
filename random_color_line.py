import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import colormap as cm

class Particle(object):
    def __init__(self,x,y,velocity):

        self.position = np.array([x,y])
        self.velocity = velocity
        assert len(self.velocity)==2


    def move(self):
        self.position= np.add(self.velocity, self.position)
    def accelerate(self,a):
        self.velocity=np.add(self.velocity,a)

def random_accelerator(magnitude):
    return np.array([ np.random.uniform(-magnitude,magnitude), np.random.uniform(-magnitude,magnitude)])

def point_repulsor(magnitude,position,particle):
    norm=np.linalg.norm(particle-position)

    return magnitude/(norm**2)*(particle-position)





if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    background_color = [1, 1, 1, 1]
    foreground_color = [(149/255, 131/255, 189/255, 0.01)]
    image_size = 1000
    UNIT=1.0/image_size
    number=1000# number of particles in the system
    particles=[None]*number
    for i in range(number):
         particles[i] = Particle(0.5, 0.5, [0,0])

    total_steps=500

    cm_subsection = np.linspace(1,0, total_steps)
    foreground_colors = cm.random_colormap(2,total_steps,even=False,alpha=0.01)



    def step_function(self):
        # render.clear_canvas()
        for particle in particles:
            pos=particle.position
            particle.move()
            self.circle(pos[0],pos[1],3*self.unit)
            particle.accelerate(random_accelerator(UNIT/5))#+ point_repulsor(UNIT/200,np.array([0.5,0.6]),pos))
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
