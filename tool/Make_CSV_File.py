
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:12:28 2019

@author: ChengZhenfeng
"""
import os
#import csv

# 生成存储图像的.csv文件
f=open("TrianMask.csv","w") #没有文件的话自己就会新建了！
# csvwriter = csv.writer(f,dialect = ("excel"))
# path="/home/chengzhenfeng/PycharmProjects/program/venv/czf1/Unet2d-master/Dataset/GlandCeildata/train/Image"
path="/home/chengzhenfeng/PycharmProjects/program/venv/czf1/Unet2d-master/Dataset/GlandCeildata/train/Mask"
#path="D:\\opencv_python_file\\opencv3计算机视觉python语言实现\\"
k=os.listdir(path)  #获取指定文件夹下面的文件

for files1_name in k:
    save_name= path + "/" + files1_name
    al=save_name
    f.write(al+"\n")

f.close()
