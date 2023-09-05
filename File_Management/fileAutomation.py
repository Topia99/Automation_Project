import os
from os.path import splitext, exists, join
import shutil

import time

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



source_dir = "/Users/jasonzeng/Downloads"
dest_dir_sfx = "/Users/jasonzeng/Documents/Download Files/Sound"
dest_dir_music = "/Users/jasonzeng/Documents/Download Files/Sound/music"
dest_dir_video = "/users/jasonzeng/Documents/Download Files/Video"
dest_dir_image = "/Users/jasonzeng/Documents/Download Files/Images"

def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
        
    return name
    

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.pmg'):
                    dest = dest_dir_image
                    move(dest, entry, name)





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()