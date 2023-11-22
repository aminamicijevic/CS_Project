try:
    my_file = open('notAfile.txt')
except FileNotFoundError:
    print("File does not exist")
