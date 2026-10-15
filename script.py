import os
import cv2
import numpy as np

data_dir = 'data'
if os.path.exists(data_dir):
    for f in os.listdir(data_dir):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(data_dir, f)
            img = cv2.imread(path)
            if img is not None:
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, np.array([0,120,70]), np.array([10,255,255])) + cv2.inRange(hsv, np.array([170,120,70]), np.array([180,255,255]))
                cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                sayi = sum(1 for c in cnts if cv2.contourArea(c) > 500)
                print(f"{f} -> Hedef: {sayi}")
else:
    print("Data klasörü bulunamadı!")

