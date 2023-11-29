import json
import os
from xml.dom import minidom


def process_all_jpg_files(dir_path):
    i = 0
    for f in os.listdir(dir_path):
        json_filepath = os.path.join(dir_path, f)
        xml_filepath = os.path.join(dir_path.replace("json", "xml"), f.replace("json", "xml"))
        print("jsonFile:",json_filepath, xml_filepath)
        #print(output)
        with open(json_filepath, "r") as fd:
            obj_list = json.load(fd)
            #print(type(obj_list), obj_list)
            
            xml_str = create_xml(obj_list)
            #print(xml_str)
            with open(xml_filepath, "w") as xml_fd:
                xml_fd.write(xml_str)
        #break



def create_xml(input_list):
 
    # we make root element
    root = minidom.Document()

    objectsList = root.createElement('objects')
    root.appendChild(objectsList)
 
    for obj in input_list:
        object = root.createElement('object')
        object.setAttribute('label', obj['label'])
        object.setAttribute('score', str(obj['score']))
        object.setAttribute('x1', str(obj['box'][0]))
        object.setAttribute('y1', str(obj['box'][1]))
        object.setAttribute('x2', str(obj['box'][2]))
        object.setAttribute('y2', str(obj['box'][3]))

        objectsList.appendChild(object)
    
    xml_str = root.toprettyxml(indent="\t")
 
    return xml_str


dir_path = "./json_output"
process_all_jpg_files(dir_path)
