import cv2
import numpy as np

def preprocessImage(img):
    #initialize norm_img 
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    #normalize the image
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    return img
