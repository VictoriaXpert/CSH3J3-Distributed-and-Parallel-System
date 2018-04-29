import threading
import os
import time


class DirectoryCrawler(threading.Thread):
    def __init__(self, dirName, fileList):
        threading.Thread.__init__(self)
        self.dirName = dirName
        self.fileList = fileList

    def run(self):
        for fname in self.fileList:
            handle.write("%s\n" % os.path.abspath(
                os.path.join(self.dirName, fname)).encode('utf-8'))


start = time.time()
handle = open("test.txt", "w")
writers = []

rootDir = '/'
for dirName, subdirList, fileList in os.walk(rootDir):
    current = DirectoryCrawler(dirName, fileList)
    current.start()


handle.close()
end = time.time()
print(end-start)
