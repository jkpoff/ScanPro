import cv2
from matplotlib import pyplot as plt
import numpy as np

class CV():
    def __init__(self, img):
        self.img = cv2.imread(img)

    def grayscale(self, threshLvl):
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./images/gray.jpg", gray_image)
        thresh, im_bw = cv2.threshold(gray_image, threshLvl, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./images/bw_image.jpg", im_bw)
        return "./images/bw_image.jpg"

    def noise_reduction(self):
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(self.img, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.erode(self.img, kernel, iterations=1)
        image = cv2.morphologyEx(self.img, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(self.img, 3)
        
        cv2.imwrite("./images/no_noise.jpg", image)
        return "./images/no_noise.jpg"
    
    



