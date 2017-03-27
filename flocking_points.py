import os
import cairo as cairo
import numpy as np
from render import Animate, Image_Creator
import colormap as cm

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
def angle_between(v1,v2):
    dot=np.dot(v1,v2)/np.linalg.norm(v1)/np.linalg.norm(v2)
    return np.arccos(np.clip(dot,-1,1))
def rotate_angle(v,angle):
    m=np.array([[np.cos(angle),-np.sin(angle)], [np.sin(angle),np.cos(angle)]])
    return m.dot(v)


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
            angle=angle_between(group_velocity,target_boid.velocity)
            rotated=rotate_angle(target_boid.velocity, -angle*self.alignment_scaling)
            return rotated - target_boid.velocity
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

def flock_burst(background_color = [1, 1, 1, 1],colors=[],
                image_size = [400,300], number=10, total_steps=200,
                number_of_colors=2, alpha=0.1,even=True,
                show=True,save=False,fname='test.png',particle_size=1):

    unit=1.0/max(image_size)
    positions=[None]*number
    velocities=[None]*number
    for i in range(number):
        positions[i] = [np.random.uniform(0,1), np.random.uniform(0,1)]
        velocities[i] = [np.random.uniform(0,1)*unit, np.random.uniform(0,1)*unit]





    if colors==[]:
        foreground_colors = cm.random_colormap(number_of_colors, total_steps, even=even, alpha=alpha)
    else:
        if even:
            spacing=np.linspace(0,total_steps,num=len(colors),dtype=int)
            colors=[np.append(x,alpha) for x in colors]
        foreground_colors=cm.polylinear_gradient(colors, spacing,total_steps,alpha=alpha)
    # [seperation , alignment , com]
    flock = BoidFlock(positions, velocities, [0.1,0.1,0.1], np.multiply(unit,[10,50,50]),unit)

    def step_function(self):
        print("step")
        flock.move_flock()
        for boid in flock.boids:
            pos=boid.position
            self.circle(pos[0],pos[1],particle_size*self.unit)
            #boid.accelerate(random_accelerator(unit/5))
        return True



    if show:
        # These are the bits that need to be run when calling the Animation
        render = Animate(image_size, background_color, foreground_colors, step_function, interval=100, save=save, stop=total_steps)
        render.start()

    else:
        #this is what needs to be run to produce an image without animation
        image=Image_Creator(image_size, background_color, foreground_colors, step_function, stop=total_steps)
        image.create()
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    flock_burst()
