import cv2
import os
import tempfile, requests


def mp4_to_jpgs(mp4_filepath, jpg_prefix):
    print("Func called")
    try:
        vidcap = cv2.VideoCapture(mp4_filepath)
        #print(vidcap.get(cv2.CAP_PROP_FOURCC))
        print(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
        success,image = vidcap.read()
        print(success)
        count = 0
        while success:
            cv2.imwrite(jpg_prefix+"_%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            #print('Read a new frame: ', success)
            if count % 250 == 0:
                print("Frames printed:", count)
            count += 1
        print("Total Frames printed:", count)
    except Exception as e:
        print("Some error occured,", e)

def details_mp4(mp4_filepath):
    print("Func called:", mp4_filepath)
    if os.path.exists(mp4_filepath):
        print("File Found:", mp4_filepath)
    try:
        vidcap = cv2.VideoCapture(mp4_filepath)
        #print(vidcap.get(cv2.CAP_PROP_FOURCC))
        print(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
        success,image = vidcap.read()
        print(success)
        
    except Exception as e:
        print("Some error occured,", e)


    
mp4_to_jpgs(
    mp4_filepath='./earthcam_dublin.mp4',
    jpg_prefix='./extra/mp4_files/jpg_frames/jpg'
)
