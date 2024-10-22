from os import listdir, replace as replace_file, system, name as osname
from os.path import isfile, join
from pathlib import Path

# Strings
NEW_NAME_INPUT = "New File Name (Leave Empty To Not Change): "
CATEGORY_INPUT = "Category (/ For uncategorized) (Empty For Last): "
FILENAME_HEADER = lambda file: f"Current File Name: {file}\n"
EMPTY_STRING = ""
DOT = "."
# Strings

# Directories
INPUT_FOLDER = "./in"
OUTPUT_FOLDER = "./out"
# Directories

def main():
  clear_stdout() # Just To Make Sure There Isn't A ./main.py Hanging At The Top

  files = [f for f in listdir(INPUT_FOLDER) if isfile(join(INPUT_FOLDER, f))]
  last_category = "uncategorized"

  for file_name in files:
    file_path = f"{INPUT_FOLDER}/{file_name}"

    print(FILENAME_HEADER(file_name))
    name = input(NEW_NAME_INPUT).strip() or file_name

    category = input(CATEGORY_INPUT).strip() or last_category
    category = "uncategorized" if category == "/" else category
    last_category = category
    category_path = f"{OUTPUT_FOLDER}/{category}"

    # Generate The Folder For That Category
    Path(category_path).mkdir(parents=True, exist_ok=True)

    # Only Adds The Extension When There Is A Custom Name
    file_extension = f"{DOT + file_name.split(DOT)[len(file_name.split(DOT))-1] if file_name != name else EMPTY_STRING}"
    new_filename = f"{name}{file_extension}"
    replace_file(file_path, f"{category_path}/{new_filename}")

    clear_stdout()

def clear_stdout():
  system('cls' if osname == 'nt' else 'clear')

if __name__ == "__main__":
  main()