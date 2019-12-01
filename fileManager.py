from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

imagePath = 'Images'
videoPath = 'Videos'
docPath = 'Documents'
otherPath = 'Others'

imageExt = ['.png', '.jpeg']
videoExt = ['.mp4', '.wave', '.mkv']
docExt = ['.txt']
pythonPath = 'Py'

'''
dir = os.listdir('/home/mimib00/Desktop/MyFolder')

for file in dir:
    filename, ext = os.path.splitext('/home/mimib00/Desktop/MyFolder/'+file)
    print(os.path.basename(filename))
    print(filename[-len(ext)-1:])
    print(ext)
'''


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder_to_track):
            tstFileName, ext = os.path.splitext(
                '/home/mimib00/Desktop/MyFolder/'+file)
            fileName = os.path.basename(tstFileName)
            if ext in imageExt:
                print(f'Image: {fileName+ext}')
                try:
                    src = folder_to_track + "/" + fileName + ext
                    new_destination = folder_destination + "/" + imagePath + '/' + fileName + ext
                    os.rename(src, new_destination)
                except:
                    os.mkdir(folder_destination+'/'+imagePath)
                    os.rename(src, new_destination)

            elif ext in videoExt:
                print(f'Video: {fileName + ext}')
                try:
                    src = folder_to_track + "/" + fileName + ext
                    new_destination = folder_destination + "/" + videoPath + '/' + fileName + ext
                    os.rename(src, new_destination)
                except:
                    os.mkdir(folder_destination+'/'+videoPath)
                    os.rename(src, new_destination)

            elif ext in docExt:
                print(f'Doc: {fileName + ext}')
                try:
                    src = folder_to_track + "/" + fileName + ext
                    new_destination = folder_destination + "/" + docPath + '/' + fileName + ext
                    os.rename(src, new_destination)
                except:
                    os.mkdir(folder_destination+'/'+docPath)
                    os.rename(src, new_destination)
            else:
                print(f'Other: {fileName + ext}')
                try:
                    src = folder_to_track + "/" + fileName + ext
                    new_destination = folder_destination + "/" + otherPath + '/' + fileName + ext
                    os.rename(src, new_destination)
                except:
                    os.mkdir(folder_destination+'/'+otherPath)
                    os.rename(src, new_destination)


folder_to_track = "/home/mimib00/Desktop/MyFolder"
folder_destination = "/home/mimib00/Desktop/OtherFolder"
#folder_to_track = "C:/Users/hp/Desktop/MyFolder"
#folder_destination = "C:/Users/hp/Desktop/OtherFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join
