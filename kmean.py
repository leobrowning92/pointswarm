from PIL import Image
import numpy as np




def imageto_array(image_path,v=False):
    im = Image.open(image_path)
    arrayim =  np.asarray(im)
    if v:
        print(im.size,im.format,im.mode)
        print(arrayim.shape)
    return arrayim


im=imageto_array("testimage.jpg",v=True)
