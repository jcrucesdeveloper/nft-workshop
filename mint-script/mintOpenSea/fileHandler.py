
# Read and 
class FileHandler():

    def __init__(self, file_name):
        self.file_name = file_name

    def openFileRead(self, file_name):
        self.file = open(file_name,'r')

    def openFileWrite(self, file_name):
        self.file = open(file_name,'w')

    def openFileAppend(self, file_name):
        self.file = open(file_name, 'a')

    def writeFile(self, content):
        self.file.write(content)

    def closeFile(self):
        self.file.close()

    def readFile(self):
        f_open = open()





