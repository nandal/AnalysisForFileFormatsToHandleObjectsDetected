from ultralytics import YOLO
from os import listdir
from os.path import isfile, join
import json, time


def detect_objects_in_jpg(model, jpg_filepath):
    output_list = []
    results = model.predict(jpg_filepath)
    if results:
        result = results[0]
        for box  in result.boxes:
            detected_obj = {}
            detected_obj['label'] = result.names[box.cls[0].item()]
            detected_obj['score'] = box.conf[0].item()
            detected_obj['box'] = box.xyxy[0].tolist()
            #print(detected_obj)
            output_list.append(detected_obj)
    return output_list



def detect_objects_in_jpg(model):
    jpg_files = []
    for i in range(1, 17):
        jpg_files.append(f"jpg_frames/jpg_{i}.jpg")
    output_list = []
    results = model.predict(jpg_files)
    print("Total Files processed:", len(jpg_files))
    print("Total Files processed:", len(results))
    #return output_list


def process_all_jpg_files(model, dir_path):
    i = 0
    #onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for f in listdir(dir_path):
        output = detect_objects_in_jpg(model, join(dir_path, f))
        json_filename = f.replace("jpg", "json")
        #print(output)
        with open(f"json_output/{json_filename}", "w") as fd:
            fd.write(json.dumps(output, indent=2))
            i += 1
            if i%100==0:
                print(f"{i} images are processed")


# model = YOLO("yolov8n.pt")  # Nano
# model = YOLO("yolov8s.pt")  # Small
# model = YOLO("yolov8m.pt")  # Medium
# model = YOLO("yolov8l.pt")  # Large
stime = time.time()
model = YOLO("yolov8x.pt") # Huge

images_dir='./extra/mp4_files/jpg_frames'
process_all_jpg_files(model, images_dir)

print(f"Time Taken: {time.time()-stime}")


