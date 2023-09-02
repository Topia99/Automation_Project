import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


source_dir = "/Users/jasonzeng/Downloads"
dest_dir_sfx = "/Users/jasonzeng/Desktop/Sound"
dest_dir_music = "Users/jasonzeng/Desktop/Sound/music"
dest_dir_video = "users/jasonzeng/Desktop/Downloaded Video"
dest_dir_image = "/Users/jasonzeng/Desktop/Downloaded Images"



class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
















if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()