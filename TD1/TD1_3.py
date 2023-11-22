import os
import datetime

# Path to the data_files folder
data_files_path = r"C:\Users\amina\Downloads\TD_1\data_files"

# Listing all items in data_files_path
all_items = os.listdir(data_files_path)

# Initializing an empty list to store folder paths
folder_paths = []

# Filtering all items in a path to include only directories but not folder_1 and storing those items in a list

# This could be solved using list comprehension like this:
# folder_paths = [os.path.join(data_files_path, folder) for folder
# in all_items if os.path.isdir(os.path.join(data_files_path, folder)) and folder != "folder_1"]

for i in all_items:
    item_path = os.path.join(data_files_path, i)
    if os.path.isdir(item_path) and i != "folder_1":
        folder_paths.append(item_path)

# Printing out the created list of paths
print("Folder paths in data_files (excluding folder_1):")
for i in folder_paths:
    print(i)


# Defining a custom sorting key function
def numeric_sort_key(folder_name):
    # Extracting the numeric portion of the folder name and converting it to an integer
    return int(folder_name[-2:])


# Sorting the folder paths using the custom sorting key function
folder_paths.sort(key=numeric_sort_key)

# Initializing an empty list to store StatsGate.txt paths
statsgate_paths = []

# Finding the StatsGate.txt files in each folder

# This could also be solved using list comprehension, like this:
# statsgate_paths = [os.path.join(folder, "StatsGate.txt") for folder
# in folder_paths if os.path.exists(os.path.join(folder, "StatsGate.txt"))]

for i in folder_paths:
    statsgate_file = os.path.join(i, "StatsGate.txt")
    if os.path.exists(statsgate_file):
        statsgate_paths.append(statsgate_file)

# Printing out the sorted paths
print("StatsGate.txt paths sorted by folder name:")
for path in statsgate_paths:
    print(path)

# Adding the line at the end

# This could also be solved using list comprehension, like this:
# [open(path, 'a').write(f"This file was file number {i}.\n") for i, path in enumerate(statsgate_paths, start=1)]

for i, path in enumerate(statsgate_paths, start=1):
    with open(path, 'a') as file:
        file.write(f"This file was file number {i}.\n")

# Replacing by selecting the line by index
folder_1_path = os.path.join(data_files_path, "folder_1")
statsgate_file_path = os.path.join(folder_1_path, "StatsGate.txt")

# Getting the today's date
todays_date = datetime.date.today()
todays_date_string = todays_date.strftime("%d.%m.%Y.")

# Reading the contents of the file
with open(statsgate_file_path, 'r') as file:
    lines = file.readlines()

# Replacing the line by index (assuming it's the 9th line)
if len(lines) >= 2:
    lines[8] = f"# StartDate = {todays_date_string}\n"

# Writing the modified contents back to the file
with open(statsgate_file_path, 'w') as file:
    file.writelines(lines)

# Replacing by automatically finding the line that starts with StartDate

# This could also be solved using list comprehension, like this:
# lines = [f"# StartDate = {todays_date_string}\n" if line.startswith("# StartDate =") else line for line in file]

lines = []
with open(statsgate_file_path, 'r') as file:
    for i in file:
        if i.startswith("# StartDate ="):
            lines.append(f"# StartDate = {todays_date_string}\n")
        else:
            lines.append(i)

# Writing the modified contents back to the file
with open(statsgate_file_path, 'w') as file:
    file.writelines(lines)
