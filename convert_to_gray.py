import os
import cv2
import numpy as np

input_path = "./images"
output_path = "./gray"

for img in os.listdir(input_path):
    print(img)
    image = cv2.imread(os.path.join(input_path, img))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.merge([gray,gray,gray])
    cv2.imwrite(os.path.join(output_path, img), gray)