#Requiremnt-2

def readFile(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
            print("File Contents:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")


# readFile("test.txt")

###############################################################################################
#Requiremnt-2

def writeNewFile(path, data):
    try:
        with open(path, 'w') as file:
            for line in data:
                file.write(line + '\n')
        print(f"Data written successfully to {path}.")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{path}'.")


data = ["Hello, World!", "Python", "End of file."]
# writeNewFile("newFile.txt", data)
# readFile("newFile.txt")

###############################################################################################
#Requiremnt-2

def modifyAndCopyFile(srcPath, destPath):
    try:
        # Reading from the source file
        with open(srcPath, 'r') as sourceFile:
            content = sourceFile.readlines()

        # Modifying content
        modifiedContent = [line.upper() for line in content]

        # Writing to the destination file
        with open(destPath, 'w') as destinationFile:
            destinationFile.writelines(modifiedContent)

        print(f"Successfully modified and written to {destPath}.")
    except FileNotFoundError:
        print(f"Error: The source file '{srcPath}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for file operations.")


# readFile("test.txt")
# modifyAndCopyFile("newFile.txt", "test.txt")
# readFile("test.txt")

