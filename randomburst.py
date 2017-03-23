from random_color_line import point_burst
import sys, os
# this file is meant to be scripted.
# it takes the following arguments in this order
# save directory filename
#print(sys.argv)
save=os.path.join(sys.argv[1],sys.argv[2])
print(save)
point_burst(background_color = [0.1,0.1,0.1,1], number_of_colors=3, particle_size=2, number=100, total_steps=300, image_size=[600,400], save=True, fname=save, show=False)
