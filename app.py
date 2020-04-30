import os
import re
import shutil
from pathlib import Path


def directory_spider(input_dir, file_pattern, maxResults):
    file_paths = []
    showAll = False
    for dirpath, dirnames, filenames in os.walk(input_dir):
        file_list = []
        for item in filenames:
            if not file_pattern:    # get all, if not defined
                file_list.append(item)
            elif re.search(file_pattern, item):
                file_list.append(item)
        file_path_list = []
        for item in file_list:
            file_path_list.append(os.path.join(
                dirpath, item).replace("\\", "/"))
        file_paths += file_path_list
        if maxResults:  # if defined
            if len(file_paths) > int(maxResults):
                break
        else:
            showAll = True
    if showAll:
        output_file_paths = file_paths
    else:
        last_element = int(maxResults)
        output_file_paths = file_paths[0:last_element]
    # get certain number of elements of the file_paths array
    # return file_paths[0:showResult]
    return output_file_paths


# input_dir = "test_folder"
user_input_dir = input("Enter directory path: ")
file_pattern = input("Enter file_pattern: ")
maxResults = input("Number of results: ")
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
        print("\n")
        print(target + " copied to " + copy_dir + ";")


def move_func(output):
    move_dir = 'move_dir'
    print("\n")
    isSure = input("Are you sure to move? Y/N: ")
    if isSure == 'Y':
        if not os.path.isdir(move_dir):
            Path(move_dir).mkdir(parents=True, exist_ok=True)
            print(move_dir + " directory created.\n")
        for target in output:
            shutil.move(target, move_dir)
            print(target + " moved to " + move_dir + ";")
    else:
        print("Move operation canceled.")


def remove_func(output):
    print("\n")
    isSure = input("Are you sure to delete? Y/N: ")
    if isSure == 'Y':
        for target in output:
            os.remove(target)
            print(target + "    ## deleted.")
    else:
        print("Delete Canceled.")


copy_func(output)
# move_func(output)
# remove_func(output)
