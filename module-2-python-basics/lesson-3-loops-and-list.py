"""
Module 2 — Activity: File Sorting with os and shutil
Student: Kimber John F. Patio
Date: September 25, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a simple file sorting program using os and shutil.
The program checks the files in a folder and moves them
into folders based on their file type, such as Images,
Documents, and Others.


============================================
KEY VOCABULARY
============================================
- os module: used to work with files and folders
- shutil module: used to move and manage files
- file path: the location of a file
- directory: a folder that contains files


============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

folder = "my_files"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension in [".jpg", ".png", ".gif"]:
            destination = os.path.join(folder, "Images")
        elif extension in [".txt", ".pdf", ".docx"]:
            destination = os.path.join(folder, "Documents")
        else:
            destination = os.path.join(folder, "Others")

        os.makedirs(destination, exist_ok=True)
        shutil.move(file_path, os.path.join(destination, file))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A mistake I want to avoid is using the wrong folder
path. If the folder name or location is incorrect,
the program may not find the files.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

"""
