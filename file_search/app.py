import glob

filename_to_search = str(input("Enter the filename to search: ")).lower()
# start_dir = ('/Volumes/Sandbox/ProjectPy/')
start_dir = str(input("Enter the start directory to search: "))

symbol = '/*'

def search_files_by_fullname(dirs_list,filename_to_search=''):
        for file in dirs_list:
            # print(file)
            if filename_to_search.lower() in file:
                print(f"Found {filename_to_search} in {file}")
                print("Continue to search...")


while True:
    try:
        files = glob.glob(start_dir + symbol, recursive=True)
        search_files_by_fullname(files,filename_to_search)
        symbol += '/*'
    except RecursionError as e:
        print("Search is ended!")
        break
