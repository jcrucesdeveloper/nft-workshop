import json

class FileHandler():

    def __init__(self, file_name):
        self.file_name = file_name

    def openFileRead(self):
        self.file = open(self.file_name,'r')

    def openFileWrite(self):
        self.file = open(self.file_name,'w')

    def openFileAppend(self):
        self.file = open(self.file_name, 'a')

    def readFile(self):
        content = self.file.read()
        return content

    def readFileLines(self):
        lines = []

        for line in self.file:
            lines.append(line)
        return lines

    def readFileLines(self, n_lines) :
        lines = []

        for n in range(n_lines):
            line = self.file.readline()

            if line == '':
                break

            lines.append(line)
        
        return lines

    def readJSONFile(self):
        json_info = json.load(self.file)
        return json_info

    def readJSONField(self,field_name):
        json_info = self.readJSONFile()
        return json_info[field_name]
        

    # Write methods
    def writeFile(self, content):
        self.file.write(content)

    def closeFile(self):
        self.file.close()






    




