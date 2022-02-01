
class FileHandler():



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




