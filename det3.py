# -*- coding: utf-8 -*-
import cv2
import sys
import imutils
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
 
if __name__ == '__main__' :
 
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[7]
 
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()
 
    
    video = cv2.VideoCapture("1.MOV")
 
   
    if not video.isOpened():
        print "Could not open video"
        sys.exit()
 
    
    ok, frame = video.read()
    if not ok:
        print 'Cannot read video file'
        sys.exit()
    frame = imutils.resize(frame, width=1000) 
    
    bbox = (287, 23, 86, 320)
 
   
    bbox = cv2.selectROI(frame, False)
 
    
    ok = tracker.init(frame, bbox)
 
    while True:
        
        ok, frame = video.read()
        if not ok:
            break
        frame = imutils.resize(frame, width=1000) 
       
        timer = cv2.getTickCount()
 
        
        ok, bbox = tracker.update(frame)
 
      
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
  
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
           
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        
      
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
     
       
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
        
        cv2.imshow("Tracking", frame)
 
       
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
cv2.destroyAllWindows()
