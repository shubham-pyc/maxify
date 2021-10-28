import json
import re


def get_campagin_id_from_name(campagins, name):
    ret_value = None
    if isinstance(campagins, dict):
        if "items" in campagins:
            for item in campagins["items"]:
                if item.get("name", "") == name:
                    ret_value = item
                    break
            else:
                raise IOError(
                    "Invalid campaign name: campaign with name {} does not exist".format(name))
    else:
        raise ValueError("Custom Error: Campagin is not type of dict")

    return ret_value


def read_file(path, as_json=False):
    ret_value = ""
    _file = open(path, 'r')
    if as_json:
        ret_value = json.load(_file)
    else:
        ret_value = _file.read()
    _file.close()
    return ret_value


def get_element_id_and_variant_id_from_path(file_path=""):
    #file_path = "/home/impadmin/Desktop/QA - Dummy Campaign For FSR/Source File/Element1-MTYyMDQw/variant1-MTYyMDQw-.html"

    return get_ids_from_path(file_path, 2)


def get_script_id_from_path(file_path=""):
    return get_ids_from_path(file_path, 1)


def get_ids_from_path(file_path, count=1):
    directories = file_path.split("/")

    error = ValueError(
        "Custom Error: Invalid path to extract element id and variant id {}".format(file_path))

    if len(directories) > 1:

        if count == 2:
            element_dir = directories[-2].split("-")
            variant_dir = directories[-1].split("-")
            if (len(element_dir) > 1 and len(variant_dir) > 1):
                return (element_dir[-1], variant_dir[-2])
        elif count == 1:
            script_dir = directories[-1].split("-")
            if (len(script_dir) > 1):
                return (script_dir[-2])
        else:
            raise error

    else:
        raise error


def is_script_path(file_path):
    regex = "campaign scripts"
    if re.search(regex, file_path):
        return True
    return False
