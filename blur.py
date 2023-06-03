import os
import cv2
import numpy as np

input_path = "./images"
output_path = "./GaussinBlur"
os.mkdir(output_path)

for img in os.listdir(input_path):
    image = cv2.imread(os.path.join(input_path, img))
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(os.path.join(output_path, img), blur)