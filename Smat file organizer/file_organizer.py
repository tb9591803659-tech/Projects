
import os 
import shutil 

def file_detector(extension) :
    if extension in [".jpg",".png"] :
        
        return "Image"
    elif extension in [".mp4"] :
        
        return "Video"
    elif extension in [".mp3"] :
        
        return "Audio"
    else :
        
        return "Other"
    
def file_mover(file,directory) :
    name, extension = os.path.splitext(file)
    category = file_detector(extension)
    source = os.path.join(directory,file)
    if not os.path.isfile(source):
        return
    destination_folder = os.path.join(directory,category)
    os.makedirs(destination_folder,exist_ok=True)
    destination = os.path.join(destination_folder,file)
    print("From:",source)
    print("To:",destination)
    shutil.move(source,destination)
    print(f"Moved{file}->{category}")

directory = input("Enter the path: ")

files = os.listdir(directory)

for file in files :
    name, extension = os.path.splitext(file)
    category = file_detector(extension)
    print(file , " -> ", category)
    
    file_mover(file,directory)

    

