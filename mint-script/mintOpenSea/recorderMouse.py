from fileHandler import FileHandler

# Need sudo for these two
import time, keyboard, pyautogui

class RecorderMouse():
    
    def __init__(self, record_file_name):
        self.record_number = 0
        self.record_file = FileHandler(record_file_name)

    def openRecorderWriteMode(self):
        self.record_file.openFileWrite()
    
    def openRecorderAppendMode(self):
        self.record_file.openFileAppend()


    def printPosition(self):
        (x,y) = pyautogui.position()
        print('Pos x: {xcord}, Pos y: {ycord} '.format(xcord=x,ycord=y))

    def writePositionInFile(self):
        """ Write record number and position (x and y cords) of the mouse """
        
        record_number_str = 'RECORD NUMBER {number}\n'.format(number = self.record_number)

        (x,y) = pyautogui.position()
        position_str = 'Pos x: {xcord}, Pos y: {ycord} \n'.format(xcord=x,ycord=y)
        
        self.record_file.writeFile('\n\n')
        self.record_file.writeFile('********************************************************************')
        self.record_file.writeFile(record_number_str)
        self.record_file.writeFile('\n\n')
        self.record_file.writeFile('********************************************************************')
        self.record_file.writeFile(position_str)

        self.record_number = self.record_number + 1


    def closeRecorder(self):
        self.record_file.closeFile()



if __name__ == '__main__':

    recorder = RecorderMouse('key_records.txt')
    recorder.openRecorderWriteMode()

    while True:
        time.sleep(0.05)

        recorder.printPosition()
        if keyboard.is_pressed("r"):
            print("RECORDED")
            recorder.writePositionInFile()
    
    recorder.closeRecorder()
        






    

