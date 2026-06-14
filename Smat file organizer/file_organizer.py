
import os 

def file_detector(extension) :
    if extension in [".jpg",".png"] :
        print("Image")
    elif extension in ["mp4"] :
        print("Video")
    elif extension in ["mp3"] :
        print("Audio")
    else :
        print("Other document")
    
files = os.listdir()

for file in files :
    name, extension = os.path.splitext(file)
    print("Filename =",name," Extension =",extension)
    file_detector(extension)
    

