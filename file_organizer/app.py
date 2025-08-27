import os
import shutil

path_to_directory = input("path to directory: ")

# Remove symbol '\' in path, if drag and drop method used
if '\\' in path_to_directory:
    path_to_directory = path_to_directory.replace('\\', '')
# If last character is space remove it
while path_to_directory[-1] == ' ':
    path_to_directory = path_to_directory[:-1]

def orginize_directory(path):
    for file in os.listdir(path):
        # Pass if path + file is directory
        if os.path.isdir(os.path.join(path, file)):
            continue

        # Extract file extension and format directory name
        # splitext split full filename for name and extenstion
        # https://docs.python.org/3.12/library/os.path.html#os.path.splitext
        filename, file_extension = os.path.splitext(file)
        # Remove dot in extenstion [1:] and capitalize .upper()
        directory = file_extension[1:].upper()
        # If directory False
        if not directory:
            directory = "Other"

        # Construct the new directory
        new_directory_path = os.path.join(path, directory)

        # Create new directory if it does not exist
        os.makedirs(new_directory_path, exist_ok=True)

        # Move file into new directory
        shutil.move(src=os.path.join(path, file), dst=os.path.join(new_directory_path, file))
        print("Moved {} --> {}".format(file, new_directory_path))


def main():
    orginize_directory(path_to_directory)
    
main()





