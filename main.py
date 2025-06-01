import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []
}

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            category = get_category(file)
            category_folder = os.path.join(folder_path, category)
            create_folder(category_folder)
            new_location = os.path.join(category_folder, file)
            shutil.move(full_path, new_location)
            print(f"✅ Moved: {file} → {category}/")

    print("🎉 Organizing complete!")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_files(path)
