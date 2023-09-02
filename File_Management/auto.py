import os


# Access the files in downloads folder
source_dir = "/users/jasonzeng/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)