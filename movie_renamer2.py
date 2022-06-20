import os
import sys
import pathlib
import imdb #run 'pip install IMDbPY' if you do not have the api

# GLOBAL VARIABLES
GLOBAL_MOVIES = {}
ia = imdb.IMDb() #calls the IMDb function to get an access object through which IMDB data can be retrieved
DIRECTORY = str(sys.argv[1])
TO_DELETE = set()


# struct for movies
class movie_struct():
    def __init__(self, key, title, year, path, recurse, failed = False):
        self.key = key
        self.title = title
        self.year = year
        self.path = path
        self.recurse = recurse
        self.absolute_path = os.path.join(path, key)
        self.failed = failed
        self.new_file_name = ''
        self.new_folder_name = ''
    def print(self):
        print(f'KEY : {self.key}\nTITLE : {self.title}\nYEAR : {self.year}\nPATH : {self.path}\nABSOLUTE : {self.absolute_path}')
        print("---------------")

def movie_details(file, path, r = 0):
    temp = text_after_year(file)
    fixed_movie_name = remove_periods(temp)
    movie = ia.search_movie(fixed_movie_name)
    if r >= 5:
        print("Movie not found")
        TO_DELETE.add(file)
        GLOBAL_MOVIES[file] = movie_struct("WILL BE DELETED", "WILL BE DELETED", "WILL BE DELETED", "WILL BE DELETED", "WILL BE DELETED", failed = True)
        return
    id = movie[r].getID() #stores the ID of the r result of the search (if r == 0 it's the first result and so on)
    movie = ia.get_movie(id) #gets the series
    if movie['kind'] == 'movie':
        GLOBAL_MOVIES[file] = movie_struct(key = file, title = movie, year = movie['year'], path = path, recurse = r)
    else:
        print("not a movie")
        movie_details(file = file, path = path, r = (r + 1))


def text_after_year(name):
    """If the string file has four numbers in a row representing a year,
       adds parenthesis around the four numbers.
       Batman 1989xRAREx1080   ---->   Batman
    """
    pointer = 0
    year = 0
    for c in name:
        pointer += 1
        if c.isdigit():
            year += 1
        else:
            year = 0
        if year == 4:
            pointer = pointer
            return name[:pointer]
    return name

def remove_periods(s):
    """Returns the string file with all periods removed
    """
    suffix = s[len(s)-4:]
    return s[:-4].replace(".", " ") + suffix

def capitalize_first_letter(s):
    return s[0].upper() + s[1:]

def fix_movie_file():
    # loops through all files directories and subdirectories
    for subdir, dirs, files in os.walk(DIRECTORY):
        for file in files:
            # deletes .txt and .exe files with "RARBG" in the filename
            if (file.endswith(".txt") or file.endswith(".exe")):
                print(f"Deleting file {file}")
                os.remove(os.path.join(subdir, file))
                continue
            
            if (file.endswith(".nfo") or file.endswith(".idx") or file.endswith(".sub")):
                print(f"Deleting {file}")
                os.remove(os.path.join(subdir, file))
                continue

            if file.endswith(".mp4") or file.endswith(".mkv"):
                movie_details(file = file, path = subdir)

def validate(key):
    if not GLOBAL_MOVIES[key].failed:
        print("Is this information correct?")
        GLOBAL_MOVIES[key].print()
        res = input()
        if res == '': # the information is correct
            title = GLOBAL_MOVIES[key].title
            year = GLOBAL_MOVIES[key].year
            ext = pathlib.Path(GLOBAL_MOVIES[key].absolute_path).suffix
            new_name = f'{title} ({year}){ext}'
        else:
            movie_details(file = key, path = GLOBAL_MOVIES[key].path, r = GLOBAL_MOVIES[key].recurse + 1)
            if key in GLOBAL_MOVIES:
                validate(key)


def main():
    if len(sys.argv) < 2:
        print("No Directory given in argument")
        exit()
    
    fix_movie_file()
    copy_keys = GLOBAL_MOVIES.keys()
    for key in copy_keys:
        validate(key)



if __name__ == "__main__":
    main()