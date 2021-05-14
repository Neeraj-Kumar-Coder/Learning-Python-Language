import os


def soldier(path, file, format):
    renamer = 1
    filepointer = open(file)
    store = filepointer.read().split("\n")
    filepointer.close()
    os.chdir(path)
    for filename in os.listdir(path):
        if filename not in store:
            if format not in filename.split("."):
                os.rename(filename, filename.capitalize())
            else:
                os.rename(filename, str(renamer) + "." + format)
                renamer += 1


if __name__ == '__main__':
    filepath = input("Enter the path of the folder you want to prettify: ")
    filename = input("Enter the name of the file with handles the excepted names: ")
    fileformat = input("Enter the format of the files which you want to number form 1: ")
    soldier(filepath, filename, fileformat)
    print("Formatting of the document is successful...")
