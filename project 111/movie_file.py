import os
import shutil

from_dir = "C:/Users/Dell/Downloads"
to_dir = "C:/Users/Dell/OneDrive/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for files in list_of_files:
    name, extension = os.path.splitext(files)
    print(name)
    print(extension)