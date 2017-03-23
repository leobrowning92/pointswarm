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

def point_burst(background_color = [0.1, 0.1, 0.1, 1],colors=[],
                image_size = [400,300], number=1000, total_steps=200,
                number_of_colors=2, alpha=0.01,even=True,
                show=True,save=False,fname='test.png',centered=True,particle_size=1):

        UNIT=1.0/max(image_size)
        # number of particles in the system
        particles=[None]*number
        if centered:
            origin = [0.5,0.5]
        else:
            origin=[np.random.uniform(0,1), np.random.uniform(0,1)]
        for i in range(number):
             particles[i] = Particle(origin, [0,0])

        if colors==[]:
            foreground_colors = cm.random_colormap(number_of_colors, total_steps, even=even, alpha=alpha)
        else:
            if even:
                spacing=np.linspace(0,total_steps,num=len(colors),dtype=int)
                colors=[np.append(x,alpha) for x in colors]
            foreground_colors=cm.polylinear_gradient(colors, spacing,total_steps,alpha=alpha)
        def step_function(self):
            # render.clear_canvas()
            for particle in particles:
                particle.move()
                self.circle(*particle.position,particle_size*self.unit)
                particle.accelerate(random_accelerator(UNIT/5,image_size))#+ point_repulsor(UNIT/200,np.array([0.5,0.6]),pos))
            return True
        if show:
            # These are the bits that need to be run when calling the Animation
            render = Animate(image_size, background_color, foreground_colors, step_function, interval=100, save=save , stop=total_steps,fname=fname)
            render.start()

        else:
            #this is what needs to be run to produce an image without animation
            image=Image_Creator(image_size, background_color, foreground_colors, step_function, total_steps,fname)
            image.create()



if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))



    point_burst(number_of_colors=3,particle_size=2,number=1000,total_steps=300,image_size=[1200,900],save=False)
