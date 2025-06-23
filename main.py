import os
import shutil

# file extensions
FILE_TYPES = {
    "Images": [".jpg", ".png"],
    "Docs": [".pdf", ".txt"],
    "Videos": [".mp4"]
}

def make_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def check_type(filename):
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    if ext in FILE_TYPES["Images"]:
        return "Images"
    elif ext in FILE_TYPES["Docs"]:
        return "Docs"
    elif ext in FILE_TYPES["Videos"]:
        return "Videos"
    else:
        return "Others"

def move_files(folder_path):
    files = os.listdir(folder_path)
    for f in files:
        full = os.path.join(folder_path, f)
        if os.path.isfile(full):
            t = check_type(f)
            new_folder = os.path.join(folder_path, t)
            make_folder(new_folder)
            dest = os.path.join(new_folder, f)
            shutil.move(full, dest)
            print("Moved", f, "to", t)

# main code
folder = input("Enter folder path: ")
move_files(folder)
