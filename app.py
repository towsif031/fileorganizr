import os
import re
import shutil


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


trash_path = 'copy_dir'
for target in output:
    # trash_path = trash_dir + os.path.basename(target)
    # shutil.copyfile(target, trash_path)
    shutil.copy2(target, trash_path)
