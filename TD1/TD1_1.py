import os

# Getting the current folder
current_folder = os.getcwd()

# Listing all items in the current folder
all_items = os.listdir(current_folder)

# Printing out all items in the current folder
print("Contents of the current folder:")
for i in all_items:
    print(i)

# Naming the new directory
new_directory_name = "new_directory"

# Creating the new directory (could probably add errors if the name of the file already exists)
os.mkdir(new_directory_name)
print(f"Directory '{new_directory_name}' created successfully.")

# Renaming the directory
even_newer_directory_name = "even_newer_directory"
os.rename(new_directory_name, even_newer_directory_name)
print(f"Directory '{new_directory_name}' has been renamed to '{even_newer_directory_name}'.")

# Creating a file and writing inside of it
file_name = "new_file.txt"
with open(file_name, 'w') as file:
    file.write("Hello, this is my new file and I am writing inside of it!\n")
print(f"The file {file_name} has been created successfully.")

# Removing the file
os.remove(file_name)
print(f"The file {file_name} has been removed.")
