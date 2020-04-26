import os
import re


def directory_spider(input_dir, file_pattern="", maxResults=2):
    file_list = []
    file_path_list = []
    for dirpath, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            file_list.append(filename)

        for file in file_list:
            if re.search(file_pattern, file):
                file_path = os.path.join(dirpath, file).replace("\\", "/")
                file_path_list.append(file_path)

        if len(file_path_list) > maxResults:
            break

    return file_path_list[0:maxResults]


# input_dir = "test_folder"
user_input_dir = input("Enter directory path: ")
file_pattern = input("Enter file_pattern: ")
maxResults = int(input("Number of results: "))
print("\n")

input_dir = user_input_dir.replace("\\", "/")
output = directory_spider(input_dir, file_pattern, maxResults)
print("\n".join(output))
