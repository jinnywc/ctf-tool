# -*- coding: cp936 -*-
import cv2
import numpy as np
import os

def lowbit(x):
    return x&0x1
png= cv2.imread("E:\������ʱ�ļ���\���汭\longmao_4573098D3590B20A758BF76FC8ABDDDB\longmao.png" , cv2.IMREAD_UNCHANGED)  #ͼƬ�ļ�
os.system("mkdir temp")
os.system("cd temp")
for i in range(0,4):
    for f in range(0,4):
        dst= cv2.bitwise_xor(lowbit(png[: ,: ,i]),lowbit(png[: ,:, f]))
        cv2.imwrite("temp/"+"xor_"+str(i)+"_"+str(f)+".png",dst*255)

for i in range(0,4):
    for f in range(0,4):
        dst= cv2.bitwise_or(lowbit(png[: ,: ,i]),lowbit(png[: ,:, f]))
        cv2.imwrite("temp/"+"or_"+str(i)+"_"+str(f)+".png",dst*255)

for i in range(0,4):
    for f in range(0,4):  
        dst= cv2.bitwise_and(lowbit(png[: ,: ,i]),lowbit(png[: ,:, f]))
        cv2.imwrite("temp/"+"and_"+str(i)+"_"+str(f)+".png",dst*255)
