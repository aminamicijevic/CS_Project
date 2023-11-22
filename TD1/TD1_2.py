import os

# Creating a file and writing inside of it
file_name = "new_file.txt"
with open(file_name, 'w') as file:
    file.write("Hello, this is my new file and I am writing inside of it!\n")
print(f"The file {file_name} has been created successfully.")

# Getting the absolute path of the created file
absolute_path = os.path.abspath(file_name)
print(f"Absolute path of file '{file_name}' is {absolute_path}.")

# Splitting the filename and the path into two strings
file_path, only_the_file_name = os.path.split(absolute_path)
print(f"Path is {file_path} and the filename is '{only_the_file_name}'.")

# Splitting the extension from the filename
file_name_base, file_extension = os.path.splitext(only_the_file_name)
print(f"Filename base is '{file_name_base}' and the extension is '{file_extension}'.")

# Checking if the path is a directory or a file
if os.path.isdir(file_path):
    print(f"'{file_path}' is a directory.")
elif os.path.isfile(file_path):
    print(f"'{file_path}' is a file.")
else:
    print(f"'{file_path}' is neither a file nor a directory.")
