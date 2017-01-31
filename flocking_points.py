import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import matplotlib.cm as cm

class Particle(object):
    def __init__(self,x,y,velocity):

        self.position = np.array([x,y])
        self.velocity = np.array(velocity)
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

class BoidFlock(object):
    """The boid flock is a collection of Particle objects with the added benifit of being able to have some flocking methods applied to it as a whole"""
    def __init__(self,positions,velocities,scalings,ranges,unit):
        assert len(positions)==len(velocities) , "the number of positions and velocities do not match"
        self.boids=[Particle(positions[i][0],positions[i][1],velocities[i]) for i in range(len(positions))]

        self.seperation_scaling=scalings[0]
        self.alignment_scaling=scalings[1]
        self.com_scaling=scalings[2]

        self.seperation_range=ranges[0]
        self.alignment_range=ranges[1]
        self.com_range=ranges[2]

        self.unit=unit


    def move_flock(self):
        for boid in self.boids:
            boid.move()
            v1 = self.get_seperation_velocity(boid)
            v2 = self.get_alignment_velocity(boid)
            v3 = self.get_com_velocity(boid)
            #print(np.isnan(v1),np.isnan(v2),np.isnan(v3))

            boid.accelerate((v1+v2+v3))




    def get_seperation_velocity(self,target_boid):
        """probably in this case the range should be >10x the scaling so as to have smothe acceleration away from one another"""
        seperation_vector=np.zeros(2)
        group = False #flag set true if there are any boids within the range
        for boid in self.boids:
            if boid !=target_boid:
                if np.linalg.norm(boid.position-target_boid.position) < self.seperation_range:
                    boid_difference=target_boid.position-boid.position

                    #the 1/norm**2 term gives i/r scaling of this vector
                    seperation_vector=seperation_vector + (boid_difference)/(np.linalg.norm(boid_difference))
                    group = True
        if group:
            return seperation_vector * self.seperation_scaling *self.unit
        else:
            return np.zeros(2)


    def get_alignment_velocity(self,target_boid):
        """the alignment velocity is a scaled unit vector, and is not scaled proportional to how different the target boids velocity is from the alignment velocity"""
        group_velocity = np.zeros(2)
        group = False #flag set true if there are any boids within the range
        for boid in self.boids:
            if boid !=target_boid:
                if np.linalg.norm(boid.position-target_boid.position) < self.alignment_range:
                    group_velocity=np.add(boid.velocity,group_velocity)
                    group = True
        if group:
            return group_velocity * self.alignment_scaling * self.unit / np.linalg.norm(group_velocity)
        else:
            return np.zeros(2)
    def get_com_velocity(self,target_boid):
        """the COM velocity is a scaled unit vector, and is not scaled proportional to how different the target boids positions is from the COM"""
        centre_of_mass = np.zeros(2)
        group = False #flag set true if there are any boids within the range
        for boid in self.boids:
            if boid !=target_boid:
                if np.linalg.norm(boid.position-target_boid.position) < self.com_scaling:
                    centre_of_mass=np.add(boid.position,centre_of_mass)
                    group = True
        com_vector=centre_of_mass - target_boid.position
        if group:
            return com_vector * self.com_scaling * self.unit / np.linalg.norm(com_vector)
        else:
            return np.zeros(2)

if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    background_color = [1, 1, 1, 1]
    foreground_color = [(149/255, 131/255, 189/255, 0.01)]
    image_size = 500
    unit=1.0/image_size
    number=20# number of particles in the system
    positions=[None]*number
    velocities=[None]*number
    for i in range(number):
        positions[i] = [np.random.uniform(0,1), np.random.uniform(0,1)]
        velocities[i] = [np.random.uniform(0,1)*unit, np.random.uniform(0,1)*unit]


    total_steps=1

    cm_subsection = np.linspace(1,0, total_steps)
    foreground_colors = [ cm.plasma(x,alpha=1) for x in cm_subsection ]

    flock = BoidFlock(positions, velocities, [0.1,0.1,0.1], np.multiply(unit,[10,100,100]),unit)

    def step_function(self):
        #print("step")
        #print(flock.boids[1].position,flock.boids[1].velocity)
        # render.clear_canvas()
        flock.move_flock()
        for boid in flock.boids:
            print(boid.position,boid.velocity)
            pos=boid.position
            self.circle(pos[0],pos[1],10*self.unit)
            #boid.accelerate(random_accelerator(unit/5))
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
