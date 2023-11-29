# AnalysisForFileFormatsToHandleObjectsDetected
It contains data and programming scripts which are used to conduct this study


## Steps to Reproduce
1. Clone this Repository to the execution environment. (Local machine or Cloud VM etc.)
2. Download Video File from https://www.kaggle.com/datasets/nandals/dublinstreetcamvideo
3. Run Script `$ python break_mp4_into_jpgs.py`. This will create JPGs frames from the downloaded MP4 File.
4. Run Script `$ python yolov8_detect_objects_in_images.py`. This script will run YOLO Object Detection Algorithm on all the JPG Frames. And generate JSON Files for each frame.
5. Run Script `$ python json_to_xml.py`. This script will create xml files for each JSON Files for same data for comparision.
6. Run Script `$ python add_metadata_to_jpgs.py`. This script will read json output of object detection and add it to each JPG frames as exif tag.
7. Run Script `$ python analyze_jpg_frames.py`. This script will analyze the JPG Frames with minimum or maximum number of objects detected. And it also create Labeled output of those objects with bounding boxes.

   
