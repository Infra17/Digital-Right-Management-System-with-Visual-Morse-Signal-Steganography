from Morse import *
import cv2

result=""
Emb=[0,0,0,0,0]

def Fun(f,i):
    while i:
        i-=1
        Emb.append(f)

def main():
    global result
    message=input("Input for the Flag String that need to be encoded (All Caps) : ")
    message=message.upper()
    #message = "DRM-PROJECT-2021"
    print("\nThe Morse code representation of the Flag String -")
    result = encrypt(message)
    print (result,'\n')
    for i in result:
        if i==".":
            Fun(1,6)
        elif i=="-":
            Fun(1,6*3)
        elif i==" ":
            Fun(0,6*2)
        Fun(0,6)
    #print(Emb)
main()
## Till Here The EMb Array is ready.

fps=25

shade_factor = 0.2
tint_factor = 0.2
def Embed(img,index):
    if Emb[index]==1:
        '''
        img[10:20,10:30]=[255,255,255] #Just to whiten the pixels
        '''
        for a in range(10,15):
            for b in range(10,20):
                R=img[a,b,0]
                G=img[a,b,1]
                B=img[a,b,2]
                if R<=100 & G<=100 & B<=100:
                    newR = R + (255 - R) * tint_factor
                    newG = G + (255 - G) * tint_factor
                    newB = B + (255 - B) * tint_factor
                    img[a,b]=[newR,newG,newB]
                else:
                    newR = R*(1-shade_factor)
                    newG = G*(1-shade_factor)
                    newB = B*(1-shade_factor)
                    img[a,b]=[newR,newG,newB]

out=None
cap= cv2.VideoCapture('video.mp4')
i=0
index=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('I/'+str(i)+'.jpg',frame)
    img = frame
    height, width, layers = img.shape
    size = (width,height)
    if out==None:
        out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    else:
        Embed(img,index)
        index+=1
        if index==len(Emb):
            index=0
        out.write(img)
        i+=1
        #if i>600:
          #  break
out.release()
cap.release()

'''
# If you turn the frames into pictures and then make a video of the pictures, This is the code.
# You have to numeric sort the images so that the images get sorted.

import glob
import re

out=None
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

index=0
for filename in sorted(glob.glob('I/*.jpg'),key=numericalSort):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    if out==None:
        out = cv2.VideoWriter('project2.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    else:
        Embed(img,index)
        index+=1
        if index==len(Emb):
            index=0
        out.write(img)
out.release()
'''


