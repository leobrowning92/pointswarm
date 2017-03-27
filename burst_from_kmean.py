from modules.random_color_line import point_burst
import os
import numpy as np

if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    colors=np.genfromtxt(fname='sourceimages/IMG_9308_kmean6.dat',skip_header=1,delimiter=',')
    #use to randomize order
    #np.random.shuffle(colors)


    point_burst(size=2,number=1000,colors=colors,total_steps=300,image_size=[1200,900],save=False,alpha =0.01)
