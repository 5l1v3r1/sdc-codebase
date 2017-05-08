import time
import datetime
import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

now = datetime.datetime.now()
#fname = now.strftime("%B-%d-%Y")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

#fname = sys.argv[1]

out = cv2.VideoWriter('../data/'+ st+'.avi', -1, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        print('writing to disk')

        #cv2.imshow('frame',frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
