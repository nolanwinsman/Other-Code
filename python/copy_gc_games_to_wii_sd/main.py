import os
import shutil
from pathlib import Path


GAMECUBE_FOLDER = r"E:\Games"
WII_GC_FOLDER = r"F:\Games"

EXTENSIONS = [".iso"]

def main():

    for subdir, dirs, files in os.walk(GAMECUBE_FOLDER):
        for file in files:
            for ext in EXTENSIONS:
                if file.endswith(ext):
                    new_wii_folder = os.path.join(WII_GC_FOLDER, Path(file).stem)
                    if '.nkit' in new_wii_folder:
                        new_wii_folder = new_wii_folder.replace('.nkit', '')

                    if not os.path.exists(new_wii_folder):
                        print(f"Creating Folder: {new_wii_folder}")
                        os.makedirs(new_wii_folder)

                    # absolute path to the gamecube folder
                    gc_game = os.path.join(subdir, file)
                    wii_game = os.path.join(new_wii_folder, 'game.iso')
                    print(f"Copying and Renaming {gc_game} to {wii_game}")
                    shutil.copy2(gc_game, wii_game)



                    





if __name__ == '__main__':
    main()
