import compare
from PIL import Image as pili
import os
import cv2
import numpy as np

wdir=""

image_handle_list=[]

for item in os.listdir(wdir):
    if item[-4:]=='.png':
        image_full_path=wdir+'/'+item
        image_handle=pili.open(image_full_path)
        image_handle_list.append(image_handle)


compare_list=[]
for i in range(len(image_handle_list)):
    for j in range(1,len(image_handle_list)):
        if i<j:
            m_norm, z_norm = compare.compare_images(np.array(image_handle_list[i]), np.array(image_handle_list[j]))
            compare_list.append([os.path.basename(image_handle_list[i].filename),os.path.basename(image_handle_list[j].filename),m_norm,z_norm])

for item in compare_list: print item
