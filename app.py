import os

for (path, dirs, files) in os.walk('test_folder'):
    print('path: ', path)
    print('folders: ', dirs)
    print('files: ', files)
    print("\n")
