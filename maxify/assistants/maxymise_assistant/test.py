import requests
import json
import os
class ConfigBuilder():
    def __init__():
        self.e_handler = handler


def scan_folder(path):
    try:
        path = os.path.join(path, "Source File")
        if os.path.isdir(path):
            variant_directory = create_obj_from_path(path, "variant")
            scripts_directory = create_obj_from_path(path, "campaign scripts")
            print(json.dumps(variant_directory, indent=4))
            print(json.dumps(scripts_directory, indent=4))

        else:
            raise FileNotFoundError("Invalid path "+path)
    except Exception as e:
        print(e)


def create_obj_from_path(path, folder_name):
    try:
        path = os.path.join(path, folder_name)
        variant_list = os.listdir(path)
        object_directory = {}
        for variant in variant_list:
            variant_path = os.path.join(path, variant)
            object_directory[variant_path] = ""
        return object_directory
    except Exception as e:
        print(e)
    return None


