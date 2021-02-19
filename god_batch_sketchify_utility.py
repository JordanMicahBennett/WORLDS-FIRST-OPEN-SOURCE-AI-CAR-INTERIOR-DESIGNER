#Partial Author: God Bennett

#Used original code which converted pictures to sketch like appearance.

#Original code converted one png at a time, and this code converts a batch given a directory.

#Original code: https://github.com/rra94/sketchify/blob/master/sketchify.ipynb

#Instructions: Change path to desired directory. Ensure files have simple naming convention like the one I prepared, so that training pairs (i.e. pics vs sketched version match).

#Why? The dataset I build consists of 2 folders, 1 containing real images of interiors, and 0 with sketched versions or fakes. The generative adversarial neural network then learns what real interiors look like by learning to construct them from these somewhat opposing datasets.

import numpy as np
import imageio
import scipy.ndimage
import os
import matplotlib.pyplot as plt

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')



def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

path = 'C:/Users/Jordan/Downloads/God/RobotizeJa/Ai-Car-Interior-Designer/interior_realistic/'
files = os.listdir(path)


for index, file in enumerate(files):
    img =os.path.join(path, file)
    s = imageio.imread(img)
    g=grayscale(s)
    i = 255-g
    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r= dodge(b,g)
    #plt.imsave(str(index).join(['content', '.jpg']), r, cmap='gray', vmin=0, vmax=255)
    plt.imsave(os.path.join(path, str(index).join(['source', '.jpg'])), r, cmap='gray', vmin=0, vmax=255)



