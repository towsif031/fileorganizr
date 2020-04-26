import os
import re
import shutil
from pathlib import Path


def directory_spider(input_dir, file_pattern="", maxResults=50):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(input_dir):
        file_list = []
        for item in filenames:
            if re.search(file_pattern, item):
                file_list.append(item)
        file_path_list = []
        for item in file_list:
            file_path_list.append(os.path.join(
                dirpath, item).replace("\\", "/"))
        file_paths += file_path_list
        if len(file_paths) > maxResults:
            break
    return file_paths[0:maxResults]


# input_dir = "test_folder"
user_input_dir = input("Enter directory path: ")
file_pattern = input("Enter file_pattern: ")
maxResults = int(input("Number of results: "))
print("\n")

input_dir = user_input_dir.replace("\\", "/")
output = directory_spider(input_dir, file_pattern, maxResults)
print("\n".join(output))


def copy_func(output):
    copy_dir = 'copy_dir'
    for target in output:
        # copy_dir = trash_dir + os.path.basename(target)
        # shutil.copyfile(target, copy_dir)
        shutil.copy2(target, copy_dir)


def move_func(output):
    move_dir = 'move_dir'
    if not os.path.isdir(move_dir):
        Path(move_dir).mkdir(parents=True, exist_ok=True)
    for target in output:
        shutil.move(target, move_dir)


# copy_func(output)
move_func(output)
