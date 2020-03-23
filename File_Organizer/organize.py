import os
from pathlib import Path

Subdirectories = {
    "Documents": ['.pdf', '.rtf', '.txt'],
    "Audio": ['.mp3', '.m4a', '.m4b'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Images": ['.jpg', '.mpeg', '.png', '.mpg', '.jpeg']
}

def pickDirectory(value):
    for category, suffixes in Subdirectories.items():
        for suffix in suffixes:
            if suffix == value:
                return (category)
    return "MISC"

def organizeDirectory():
    for file in os.listdir():
        directory = pickDirectory("." + (file.partition('.')[2]))
        if directory:
            path = Path(directory)
            if path.is_dir() != True:
                path.mkdir()
            fileDest = Path(str(path) + "/" + file)
            os.replace(file, fileDest)

organizeDirectory()