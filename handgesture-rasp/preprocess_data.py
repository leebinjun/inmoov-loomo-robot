import os
import cv2

path = "./data"
h = 28
w = 28

files = os.listdir(path) 
# print(files)

for f in files: 
    print(f)
    cnt = 0
    data_list = os.listdir(path+'/'+f)
    # print(data_list[:4])
    for data in data_list:
        data_file_path = path+'/'+f+'/'+data 
        img = cv2.imread(data_file_path)
        img_resize = cv2.resize(img, (w, h))
        cv2.imwrite(path+'/'+f+'/'+"{:04d}.jpg".format(cnt), img_resize)
        cnt += 1
    #     if cnt == 2:
    #         break
    # break

