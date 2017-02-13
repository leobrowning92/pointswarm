from PIL import Image
import numpy as np




def imageto_array(image_path,v=False):
    im = Image.open(image_path)
    im.thumbnail((256,256))
    arrayim =  np.asarray(im)
    if v:
        print(im.size,im.format,im.mode)
        print(arrayim.shape)
    return arrayim




image_array = imageto_array("testimage.jpg",v=True)
h=image_array.shape[0]
w=image_array.shape[1]
image_list=np.reshape(image_array,((h*w),3)).shape
