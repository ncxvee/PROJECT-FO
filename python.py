import os
import shutil

os.makedirs("text_files", exist_ok=True)

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, os.path.join("text_files", filename))

os.listdir("text_files")

# folder_path = input("Enter the folder path to organize: ")

# if os.path.exists():
#    print("The file exists!")
    
# else:
#    print("The file does not exist")

# list_of_files = os.listdir()
# print("All folders and file:", list_of_files)

# os.mkdir("Document")
# os.mkdir("Photo")
# os.mkdir("Video")