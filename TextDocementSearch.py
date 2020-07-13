# importing os module 
import os
import time

# identify file type to look for
pattern = '.txt'
items = os.listdir()

fileList = []
# iterate through list to find file type of .txt
for names in items:
    if names.endswith(pattern):
        # get the absolute pathname and normalize it
        namePath = (os.path.normpath(os.path.join(os.getcwd(), names)))
        # get the modified date of the list entry
        modTimesinceEpoc = os.path.getmtime(names)
        # translate the value into a standard datetimestamp
        modTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        # add item to result list
        listEntry = (namePath, '    Modified: ', modTime)
        fileList.append(listEntry)

for i in range(len(fileList)):
    print(*fileList[i])
