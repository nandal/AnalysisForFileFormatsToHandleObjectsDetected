import cv2
import json, os
import tempfile, requests




frame_number = 4941
frame_number = 11460


def find_frame_with_least_objects(score=0.5):
    dir_path = "./yolov8/json_output"
    results_dir = {} # {'frame_number': objects_count}
    for f in os.listdir(dir_path):
        json_filepath = os.path.join(dir_path, f)
        with open(json_filepath, "r") as fd:
            obj_list = json.load(fd)
            obj_count = len([x['score'] >= 0.5 for x in obj_list])
            results_dir[json_filepath] = obj_count
    max_key = max(results_dir, key= lambda x: results_dir[x])
    print("Max:", max_key, results_dir[max_key])
    min_key = min(results_dir, key= lambda x: results_dir[x])
    print("Min:", min_key, results_dir[min_key])


def get_thumbnails_of_each_objects_in_given_frame(frame_number):
    frame_info_output_dir = f"./yolov8/frame_analysis_{frame_number}"
    base_jpg_filepath = f"./yolov8/jpg_frames/jpg_{frame_number}.jpg"
    json_filepath = f"./yolov8/json_output/json_{frame_number}.json"

    if not os.path.exists(frame_info_output_dir):
        os.makedirs(frame_info_output_dir)

    obj_list = None
    
    with open(json_filepath, "r") as fd:
        obj_list = json.load(fd)
        for obj in obj_list:
            print(obj)

    base_img = cv2.imread(base_jpg_filepath)
    base_img_copy = base_img.copy()
    marked_img = base_img.copy()

    cv2.imwrite(f"{frame_info_output_dir}/base.jpg", base_img_copy)

    for obj in obj_list:
        if obj['score'] >= 0.5:
            cv2.rectangle(marked_img, (int(obj['box'][0]), int(obj['box'][1])), (int(obj['box'][2]), int(obj['box'][3])), (0, 0, 255), 2)
            cv2.putText(marked_img, obj['label'], (int(obj['box'][0]), int(obj['box'][1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


    cv2.imwrite(f"{frame_info_output_dir}/marked_with_boxes.jpg", marked_img)

# this will add bounding boxes to the given frame around the objects detected.
get_thumbnails_of_each_objects_in_given_frame(frame_number)


#find_frame_with_least_objects()
