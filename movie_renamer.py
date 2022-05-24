# TODO automates as much as possible of how I rename movie files
import os
import sys


# Global variables
DIRECTORY = str(sys.argv[1])
RENAME_ALL = False

def echo_ne(before, after):
    print(f"\n------------------------------------------------------------------------------------------")
    print(f"\t{before}\n\t{after}")
    print(f"------------------------------------------------------------------------------------------\n")

def text_after_year_folder(folder):
    """If the string file has four numbers in a row representing a year,
       adds parenthesis around the four numbers.
       Batman 1989xRAREx1080   ---->   Batman
    """
    pointer = 0
    year = 0
    for c in folder:
        pointer += 1
        if c.isdigit():
            year += 1
        else:
            year = 0
        if year == 4:
            pointer = pointer - 4
            return folder[:pointer]
    return folder


def has_year(file):
    """If the file contains four digits inside parenthesis,
       returns True
       otherwise, returns False
    """
    count = 0
    parenthesis = {'(', ')'}
    for c in file:
        if (count == 0 and c == '(') or (count > 0 and count < 5 and c.isdigit()) or (count == 5 and c == ')'):
            count += 1
        else:
            count = 0
        if count == 6:
            return True
    return False

def text_after_year(file):
    """Deletes all text after four digits inside parenthesis
       Batman (1989) 1080.mkv   --->  Batman (1989).mkv  
    """
    suffix = file[len(file)-4:]
    count = 0
    parenthesis = {'(', ')'}
    for i, c in enumerate(file):
        if (count == 0 and c == '(') or (count > 0 and count < 5 and c.isdigit()) or (count == 5 and c == ')'):
            count += 1
        else:
            count = 0
        if count == 6:
            return file[:i+1] + suffix
    return file


def parenthesis_year(file):
    """If the string file has four numbers in a row representing a year,
       adds parenthesis around the four numbers.
       Batman 1989   ---->   Batman (1989)
    """
    if has_year(file) == False:
        year = ''
        for c in file:
            if c.isdigit():
                year = year + c
            else:
                year = ''
            if len(year) == 4:
                return file.replace(year, f"({year})")
    else:
        return file

def remove_periods(file):
    """Returns the string file with all periods removed
    """
    suffix = file[len(file)-4:]
    return file[:-4].replace(".", " ") + suffix

def fix_movie_file():
    # loops through all files directories and subdirectories
    for subdir, dirs, files in os.walk(DIRECTORY):
        for file in files:
            # deletes .txt and .exe files with "RARBG" in the filename
            if (file.endswith(".txt") or file.endswith(".exe")) and "RARBG" in str(file):
                print(f"Deleting file {file}")
                os.remove(os.path.join(subdir, file))
                continue
            
            if (file.endswith(".nfo") or file.endswith(".idx") or file.endswith(".sub")):
                print(f"Deleting {file}")
                os.remove(os.path.join(subdir, file))

            if file.endswith(".mp4") or file.endswith(".mkv"):
                temp = parenthesis_year(file) # puts parenthesis around year
                temp = remove_periods(temp) # replaces periods with spaces
                temp = text_after_year(temp) # deletes all text after the year
                old_name = os.path.join(subdir, file)
                new_name = os.path.join(subdir, temp)
                if old_name != new_name:
                    echo_ne(file, temp)
                    os.rename(old_name, new_name)

def fix_movie_folder():
    for subdir, dirs, files in os.walk(DIRECTORY):
        if os.path.isdir(subdir):
            if any((fname.endswith('.mp4') or fname.endswith('.mkv')) for fname in os.listdir(subdir)):
                temp = remove_periods(subdir) # replaces periods with spaces
                temp = text_after_year_folder(temp) # deletes all text after the year, including the year
                if temp != subdir:
                    echo_ne(subdir, temp)
                    os.rename(subdir, temp)

def subtitles():
    for subdir, dirs, files in os.walk(DIRECTORY):
        for fname in files:
            if fname.endswith('.srt'):
                parent_parent = os.path.dirname(subdir)
                movie_name = ""
                if "subs" in str(subdir).lower():
                    count = len([x for x in os.listdir(subdir)])
                    if count == 1:
                        for other_fname in os.listdir(parent_parent):
                            if other_fname.endswith(".mp4") or other_fname.endswith(".mkv"):
                                movie_name = other_fname
                                new_name = f"{movie_name[:-4]}.en.srt"
                                print(f"renaming {fname} to {new_name}")
                                os.rename(os.path.join(subdir, fname), os.path.join(subdir, new_name))
                                break
                # subtitle file not inside Subs folder
                else:
                    for other_fname in os.listdir(subdir):
                        if other_fname.endswith(".mp4") or other_fname.endswith(".mkv"):
                            movie_name = other_fname
                            new_name = f"{movie_name[:-4]}.en.srt"
                            print(f"renaming {fname} to {new_name}")
                            os.rename(os.path.join(subdir, fname), os.path.join(subdir, new_name))
                            break








def main():
    if len(sys.argv) < 2:
        print("No Directory given in argument")
        exit()
    
    print("Renaming Folders and Files")
    fix_movie_file()
    fix_movie_folder()
    subtitles()
    print("Completed")



if __name__ == "__main__":
    main()