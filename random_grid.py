import os
import cairo as cairo
import numpy as np
from render import Animate

class Particle(object):
    def __init__(self,x,y,velocity):

        self.position = np.array([x,y])
        self.velocity = velocity
        assert len(self.velocity)==2


    def move(self):
        self.position= np.add(self.velocity, self.position)
    def accelerate(self,a):
        self.velocity=np.add(self.velocity,a)






if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    background_color = [1, 1, 1, 1]
    foreground_color = [149/255, 131/255, 189/255, 0.05]
    image_size = 1000
    UNIT=1.0/image_size
    number=10 # number **2 is the number of particles in the system
    particles=[None]*number*number
    for i in range(number):
        for j in range(number):
            particles[i*number+j] = Particle(0.5/number+j/number, 0.5/number+i/number, [0,0])


    def step_function(self):
        # render.clear_canvas()
        for particle in particles:
            pos=particle.position
            particle.move()
            self.circle(pos[0],pos[1],2*self.pix)
            particle.accelerate([np.random.uniform(-UNIT/10,UNIT/10),np.random.uniform(-UNIT/100,UNIT/100)])
        return True


    # These are the bits that need to be run when calling the Animation
    render = Animate(image_size, background_color, foreground_color,step_function,stop=-1,interval=100,save=False)
    render.start()
