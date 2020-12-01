import os
from os import path
import shutil

def main():
    #make a duplicate file of an existing file
    if path.exists("textfile.txt"):
        # Get path
        src = path.realpath("textfile.txt")

        # Create  backup
        dst = src + ".bak"

        # Copy over the permissions, modification times, and other info.
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # rename the original file
        os.rename("textfile.txt", "newfile.txt")

if __name__ == "__main__":
    main()