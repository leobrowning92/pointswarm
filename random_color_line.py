import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import colormap as cm

class Particle(object):
    def __init__(self,position,velocity):

        self.position = np.array(position)
        self.velocity = velocity
        assert len(self.velocity)==2


    def move(self):
        self.position= np.add(self.velocity, self.position)
    def accelerate(self,a):
        self.velocity=np.add(self.velocity,a)

def random_accelerator(magnitude,image_size):
    return np.array([ np.random.uniform(-magnitude,magnitude), np.random.uniform(-magnitude,magnitude)*image_size[0]/image_size[1]])

def point_repulsor(magnitude,position,particle):
    norm=np.linalg.norm(particle-position)

    return magnitude/(norm**2)*(particle-position)

def point_burst(background_color = [0.1, 0.1, 0.1, 1],
                image_size = [400,300], number=1000, total_steps=500,
                number_of_colors=2, alpha=0.01,even=True,
                show=True,save=False,fname='test.png'):

        UNIT=1.0/max(image_size)
        # number of particles in the system
        particles=[None]*number
        for i in range(number):
             particles[i] = Particle([0.5, 0.5], [0,0])

        foreground_colors = cm.random_colormap(number_of_colors,total_steps,even=even,alpha=alpha)

        def step_function(self):
            # render.clear_canvas()
            for particle in particles:
                particle.move()
                self.circle(*particle.position,1*self.unit)
                particle.accelerate(random_accelerator(UNIT/5,image_size))#+ point_repulsor(UNIT/200,np.array([0.5,0.6]),pos))
            return True
        if show:
            # These are the bits that need to be run when calling the Animation
            render = Animate(image_size, background_color, foreground_colors, step_function, interval=100, save=save , stop=total_steps)
            render.start()

        else:
            #this is what needs to be run to produce an image without animation
            image=Image_Creator(image_size, background_color, foreground_colors, step_function, total_steps,fname)
            image.create()



if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    point_burst()
