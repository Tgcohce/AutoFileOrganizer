import os

# Welcomes the user with their current username logged in
print(f"Welcome to Automatic File Handler {os.getlogin()}")

# We set our base location for the folder, based on input given
# This is where the folder will be created
location = input("Enter Location for folder (with the files) to be saved: ")

print("Files containing the same word will be moved to the folder, e.g. Test/Quiz/Math")

# Location of the files which we will iterate through the names of
iterloc = input("Where are the files to-be-moved located?: ")

# The common word the text files will have, the condition to be moved
COMMON_NAME = input("The common word which, to-be-moved text files contain: ")

# Setting a folder name for the folder that will store all the files
FOLDER_NAME = input("Name of Folder, the files will be stored here: ")

# Declaring a file list to hold the names of the files
file_lst = []

# setting our folders path at the given location with given name
mkdirPath = os.path.join(location, FOLDER_NAME)

# Creating the folder
os.mkdir(mkdirPath)

# Creating a directory list of all files at the given location
dir_list = os.listdir(iterloc)

# Iterating through the names of the files in dir_list
for file in dir_list:

    # Creating a target path for the file to be saved at
    targetPath = os.path.join(mkdirPath, file)

    # If the file contains the string
    if COMMON_NAME in file:

        # Add it to the file_lst to hold the name
        file_lst.append(file)

        # Move the file from (src, destination)
        # Note that we didnt need to add a "/ + file" because of our targetPath
        os.rename(iterloc + '/' + file, targetPath)


