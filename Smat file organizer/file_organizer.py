
import os 
import shutil 

def file_detector(extension) :
    extension = extension.lower()

    EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Programming": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Executables": [".exe", ".msi", ".apk"],
    "Fonts": [".ttf", ".otf"],
    "3D Models": [".obj", ".stl", ".fbx"]
    }

    for category,extensions in EXTENSION_MAP :
        if extension in extensions :
            return category
    
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
    print(f"Moved : {file}->{category}")

directory = input("Enter path :").strip().strip('"')
print("Directory entered:", repr(directory))
if os.path.isdir(directory):
    files = os.listdir(directory)

    for file in files:
        name, extension = os.path.splitext(file)
        category = file_detector(extension)
        print(file, "->", category)
        file_mover(file, directory)
else:
    print("No such directory")


    

