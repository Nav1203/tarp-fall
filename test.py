import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt 
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
model=torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')
imgs=[]
for i in range(1,4):
    temp=cv2.imread("D:\\project\\tarp_proj\\fall_dataset\\images\\val\\fall00"+str(i)+".jpg")
    imgs.append(cv2.resize(temp,(640,640)))
for i in imgs:
    res=model(i)
    cv2.imshow('YOLO',np.squeeze(res.render()))
    cv2.waitKey(0)
    df=res.pandas().xyxy[0]
    df2=res.pandas().xyxyn[0]
    #0print(df)
    for i in df['name']:
      print(i)
    for i in df2['confidence']:
       print(i)

#cv2.imshow('img',img)
#cv2.waitKey(0)