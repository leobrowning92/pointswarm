from PIL import Image
import numpy as np
from render import Show



def imageto_array(image_path,v=False):
    im = Image.open(image_path)
    im.thumbnail((256,256))
    arrayim =  np.asarray(im)
    if v:
        print(im.size,im.format,im.mode)
        print(arrayim.shape)
    return arrayim




image_array = imageto_array("testimage.jpg",v=False)
h=image_array.shape[0]
w=image_array.shape[1]
image_list=np.reshape(image_array,((h*w),3)).shape


image_size=max(h,w)

unit=1./image_size

display=Show(image_size,[[0,0,0,1]],[0.1,1,1,1])
display.start()
display.clear_canvas()
display.line([0,0.5],[1,0.5],width=unit*10)
display.expose()
