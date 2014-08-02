import os

def rename():
    for filename in os.listdir("."):
        newName = ""
        fileType = ".mp3.txt"
        if filename.endswith(".txt"):
            if filename.endswith(".mp3.txt"):
                continue
            newName = os.path.splitext(filename)[0]
            os.rename(filename, newName + fileType)

rename()

