import sys
import time
import logging
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    print("Created New File - %s." % event.src_path)

def on_deleted(event):
    print("Deleted File - %s." % event.src_path)

def on_modified(event):
    print("Modified File - %s." % event.src_path)

def on_moved(event):
    print("Moved File - %s." % event.src_path)

if __name__ == "__main__":
    patterns = ["*.html","*.htm","*.css"]
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved
    path="H:\Templates\Inspinia"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Done")
    observer.join()
