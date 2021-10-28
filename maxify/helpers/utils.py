import platform
import os
import time

def get_platform():
    ret_value = ""
    p_type = get_system_platform()
    if p_type == "windows":
        ret_value = "windows"
    elif p_type == "darwin":
        ret_value = "mac"
    else:
        ret_value = "linux"
    return ret_value

def get_system_platform():
    return platform.system().lower()

def find_folder(root="/", hop=5):
    if hop <= 0:
        return None
    try:
        dir_list = os.listdir(root)
        for dir in dir_list:
            if dir == "web-optimization":
                return os.path.join(root, "web-optimization")

        for dir in dir_list:
            path = os.path.join(root, dir)
            if os.path.isdir(path):
                ret_value =  find_folder(path, hop=hop - 1)
                if ret_value is not None:
                    return ret_value
        return None
    except Exception as e:
        pass
