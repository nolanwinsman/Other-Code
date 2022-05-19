# TODO automates as much as possible of how I rename movie files
import os
import sys

def has_year(file):
    count = 0
    parenthesis = {'(', ')'}
    for c in file:
        if (count == 0 and c == '(') or (count > 0 and count < 5 and c.isdigit()) or (count == 5 and c == ')'):
            count += 1
        else:
            count = 0
        if count == 6:
            return True
        # print(f"{c} : {count}")
    return False

def text_after_year(file):
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
        # print(f"{c} : {count}")
    return file


def parenthesis_year(file):
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
    suffix = file[len(file)-4:]
    return file[:-4].replace(".", " ") + suffix


def main():
    if sys.argv[2] == "-y":
        rename_all = True
    else:
        rename_all = False
    # directory = os.getcwd()
    # print(str(sys.argv[1]))
    directory = str(sys.argv[1])
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4") or file.endswith(".mkv"):
                # print(file)
                temp = parenthesis_year(file) 
                # print(temp)
                temp = remove_periods(temp)
                # print(temp)
                temp = text_after_year(temp)
                print('------------------------------')
                print(f"Rename:\n{file}\n{temp}")
                if rename_all:
                    response = "y"
                else:
                    response = input()
                if response == "y":
                    print("Renaming File")
                    old_file = os.path.join(subdir, file)
                    new_file = os.path.join(subdir, temp)
                    os.rename(old_file, new_file)

                else:
                    print("Skipping File")
                # print(os.path.join(subdir, file))


if __name__ == "__main__":
    main()