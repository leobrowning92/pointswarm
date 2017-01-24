import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import matplotlib.cm as cm

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
    image_size = 500
    UNIT=1.0/image_size
    number=10# number of particles in the system
    particles=[None]*number
    for i in range(number):
         particles[i] = Particle(0.5/number+i/number, np.random.uniform(0,1), [0,0])

    total_steps=200

    cm_subsection = np.linspace(1,0, total_steps)
    foreground_colors = [ cm.plasma(x,alpha=0.05) for x in cm_subsection ]



    def step_function(self):
        # render.clear_canvas()
        for primary_particle in particles:
            primary_particle.move()
            self.circle(primary_particle.position[0], primary_particle.position[1], 2*self.pix)
            for other in particles:
                #this code loop is for the particle-particle interractions
                pass



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
