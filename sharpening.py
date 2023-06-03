import os
import cv2
import numpy as np

input_path = "./images"
output_path = "./sharpen"
os.mkdir(output_path)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

for img in os.listdir(input_path):
    image = cv2.imread(os.path.join(input_path, img))
    sharpened = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(os.path.join(output_path, img), sharpened)