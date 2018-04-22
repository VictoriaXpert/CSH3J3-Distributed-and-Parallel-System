import os
import time

start = time.time()
handle = open("test.txt", "w")

rootDir = '/'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        handle.write("%s\n" % os.path.abspath(
            os.path.join(dirName, fname)).encode('utf-8'))


handle.close()
end = time.time()
print(end-start)
