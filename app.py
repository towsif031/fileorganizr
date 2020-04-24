import os

input_dir = "test_folder"

# for i in os.walk(input_dir):
#     print(i)

file_list = []
file_path_list = []
for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        file_list.append(filename)

    for file in file_list:
        file_path = os.path.join(dirpath, file)
        file_path_list.append(file_path)

# print(file_list)

print("\n".join(file_path_list))
