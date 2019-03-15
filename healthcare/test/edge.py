import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    # frame = cv2.flip(frame,1)
    edges = cv2.Canny(frame,100,200)
    # re, contours, hierachy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (255,255,255), 2)
    # img = cv2.addWeighted(frame, 0.9, edges, 0.1, 0) 
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()