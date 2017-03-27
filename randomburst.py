from modules.random_color_line import point_burst
import sys, os
# this file is meant to be scripted.
# it takes the following arguments in this order
# save directory filename
#print(sys.argv)
save=os.path.join(sys.argv[1],sys.argv[2])
back=float(sys.argv[3])
number=int(sys.argv[4])
print(save)
point_burst(background_color = [back,back,back,1], number_of_colors=3, particle_size=2, number=number, total_steps=300, image_size=[1800,1200], save=True, fname=save, show=False)
