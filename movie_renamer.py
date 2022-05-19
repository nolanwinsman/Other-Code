# TODO automates as much as possible of how I rename movie files
import os
import sys

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


def main():
    if len(sys.argv) < 2:
        print("No Directory given in argument")
        exit()
    rename_all = False
    # if user inputs -y as the third argument
    # does not prompt user 
    if len(sys.argv) >= 3:
        if sys.argv[2] == "-y":
            rename_all = True
    directory = str(sys.argv[1])
    # loops through all files directories and subdirectories
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # deletes .txt and .exe files with "RARBG" in the filename
            if (file.endswith(".txt") or file.endswith(".exe")) and "RARBG" in str(file):
                print(f"Deleting file {file}")
                os.remove(os.path.join(subdir, file))
                continue
            if file.endswith(".mp4") or file.endswith(".mkv"):
                temp = parenthesis_year(file) # puts parenthesis around year
                temp = remove_periods(temp) # replaces periods with spaces
                temp = text_after_year(temp) # deletes all text after the year
                print('------------------------------')
                print(f"Rename:\n{file}\n{temp}")
                if rename_all:
                    response = "y"
                else:
                    print("-y for yes, anything else for no")
                    response = input()
                if response == "y":
                    print("Renaming File")
                    old_file = os.path.join(subdir, file)
                    new_file = os.path.join(subdir, temp)
                    os.rename(old_file, new_file)
                else:
                    print("Skipping File")


if __name__ == "__main__":
    main()