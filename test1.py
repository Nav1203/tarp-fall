import torch
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt 
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
import sendnotification
import pyrebase
import datetime
config={
    "apiKey": "AIzaSyDJgcH85qBoOOwUxY-WsWtQFWiZwWWcaVs",
  "authDomain": "fall-det.firebaseapp.com",
  "projectId": "fall-det",
  "databaseURL": "https://fall-det-default-rtdb.firebaseio.com",
  "storageBucket": "fall-det.appspot.com",
  "messagingSenderId": "508646580821",
  "appId": "1:508646580821:web:1531df570385646532aadc"
}
model=torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')
cap = cv2.VideoCapture("http://192.168.240.76:81/stream")#"http://192.168.240.211:8080/video")#"http://192.168.240.76:81/stream")#"https://172.20.10.6:8080/video")
cnt=0
fb=pyrebase.initialize_app(config)
rl_db=fb.database()
stg=fb.storage()
unq_key=rl_db.generate_key()[1:]
start_time=time.time()
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame=cv2.resize(frame,(640,480))
        res=model(frame)
        cv2.imshow('Frame', np.squeeze(res.render()))
        cnf=res.pandas().xyxyn[0]['confidence']
        lbl=res.pandas().xyxy[0]['name']
        for i in range(0,len(lbl)):
            print(lbl[i],cnf[i])
            if(res.pandas().xyxy[0]['name'][i]=="fall detected" and res.pandas().xyxyn[0]['confidence'][i]>0.50):
                cnt+=1
        if cnt>3:
            time_stp=str(datetime.datetime.now())
            rl_db.child(unq_key).child(time_stp[:18]).set({"detected state":str(res.pandas().xyxy[0]['name'])})
            cv2.imwrite("temp.jpg",np.squeeze(res.render()))
            stg.child("images/"+unq_key+time_stp.split()[0]).put("temp.jpg")
            #img_url=stg.child("images/"+unq_key+time_stp.split()[0]).get_url(token=None)
            img_url="https://firebasestorage.googleapis.com/v0/b/fall-det.appspot.com/o/images"+f"%2F"+unq_key+time_stp.split()[0]+"?alt=media"
            sendnotification.send(img_url)
            cnt=0
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    end_time=time.time()
    if(end_time-start_time>=60):
        time_stp=str(datetime.datetime.now())
        rl_db.child(unq_key).child(time_stp[:18]).set({"detected state":str(res.pandas().xyxy[0]['name'])})
        start_time=end_time
cap.release()
cv2.destroyAllWindows()