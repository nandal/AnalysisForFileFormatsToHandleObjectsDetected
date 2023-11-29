from PIL import Image
from PIL.ExifTags import TAGS
import json, pickle, piexif, os




def add_objects_info_as_json_in_exif_tags_of_jpgs(dir_path):
    i = 0
    for f in os.listdir(dir_path):
        json_filepath = 'json_output/'+f.replace("jpg", "json")
        img_filepath = 'jpg_frames/'+f
        new_img_filepath = 'jpg_exif_tag_frames/'+f
        print(img_filepath, new_img_filepath, json_filepath)
        add_exif_tag(img_filepath, new_img_filepath, json_filepath)
        #break


def add_exif_tag(img_filepath, new_img_filepath, json_filepath):
    image = Image.open(img_filepath)

    with open(json_filepath, 'r') as fd:
        obj_list = json.load(fd)
        data = pickle.dumps(obj_list)
        exif_ifd = {piexif.ExifIFD.MakerNote: data}
        exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {},
             "thumbnail": None, "GPS": {}}
        exif_dat = piexif.dump(exif_dict)

        image.save(img_filepath)
        image.save(new_img_filepath, exif=exif_dat)


def read_exif_data(img_filepath):
    exif_dict = piexif.load(img_filepath)
    if "Exif" in exif_dict and piexif.ExifIFD.MakerNote in exif_dict["Exif"]:
        raw = exif_dict["Exif"][piexif.ExifIFD.MakerNote]
        tags = pickle.loads(raw)
        print(tags)



read_exif_data('jpg_frames/jpg_0.jpg')
# add_exif_tag('jpg_frames/jpg_0.jpg', 'jpg_exif_tag_frames/jpg_0.jpg', 'json_output/json_0.json')
# print("=================")
read_exif_data('jpg_exif_tag_frames/jpg_0.jpg')

add_objects_info_as_json_in_exif_tags_of_jpgs('jpg_frames')
