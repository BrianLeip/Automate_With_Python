# II - Automating Tasks
# 08 - Read and Write Files
# Book Examples from Chapter

import os

# Get current working directory, and join text into an OC agnostic directory string
print("*************")
print("Get current working directory, and join text into an OC agnostic directory string".upper() )
print(os.getcwd())
print(os.path.join('usr', 'bin', 'spam'))   # works with any operating system
print("*************\n")

# Creating New Folders with os.makedirs()
print("Creating New Folders with os.makedirs()".upper() )
folderString = 'C:\\ZZ-DELETE\deleteThisToo\AlsoDeleteThis'
print("-- Creating folder at: " + folderString)
# os.makedirs(folderString)     # Uncomment this to create the folders (I commented it out since it was creating them over and over)
print("*************\n")

# The os.path Module
print("*** THE os.path MODULE ***")
# os.path has many helpful functions related to filenames and file paths
# Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section. 
# The full documentation for the os.path module is on the Python website at http://docs.python.org/3/library/os.path.html

# Handling Absolute and Relative Paths
print("Handling Absolute and Relative Paths".upper() )
print(os.path.abspath('.') )    # d:\Dropbox\Programming\Courses\Python, DS\Automate with Python\08-Read Write Files
print(os.path.abspath('.\\PreMadeFolder') ) # d:\Dropbox\Programming\Courses\Python, DS\Automate with Python\08-Read Write Files\PreMadeFolder
print(os.path.isabs('.') )  # False
print(os.path.isabs(os.path.abspath('.')) ) # True
print(os.path.relpath('C:\\Windows', 'C:\\') ) # Windows
print("*************\n")

# Directory (dir) name vs base name
print("Directory (dir) name vs base name".upper() )
calcPath = "C:\Windows\System32\calc.exe"
print(os.path.basename(calcPath) ) # basename = filename = "calc.exe"
print(os.path.dirname(calcPath) ) # dirname = directory name = "C:\Windows\System32"
print(os.path.split(calcPath) ) # split has both the dirname and basename together as a tuple
print(os.path.dirname(calcPath),  os.path.basename(calcPath) )
print(os.path.split(os.path.sep) )
print("*************\n")

# Finding File Sizes and Folder Contents
print("Finding File Sizes and Folder Contents".upper() )
print(os.path.getsize(calcPath) )
calcDirPath = os.path.dirname(calcPath)
print(os.listdir(calcDirPath)[:20] )    # print the first 20 folders in C:\Windows\System32
print("Get the total size of all the files in the Windows System32 Directory:")
totalSize = 0
for filename in os.listdir(calcDirPath):
    totalSize = totalSize + os.path.getsize(os.path.join(calcDirPath, filename))
print(totalSize)