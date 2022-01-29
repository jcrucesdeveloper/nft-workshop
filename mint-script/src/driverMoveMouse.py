import pyautogui, keyboard, time

class DriverMoveMouse():

    def __init__(self):
        self.counter = 15
        self.record_number = 0
        self.collection_name = "Ratoncito Perez"
        self.collection_description = "El Ratoncito Perez es un personaje fantástico que se encarga de recoger los dientes que se les caen a los niños y que colocan bajo la almohada. Mientras los niños duermen, el ratón lo cambia por dulces, monedas u otros regalos"
        pyautogui.PAUSE = 0.5

    def move(self,x,y):
        pyautogui.moveTo(x,y)

    # Helps to record the positionc
    def printPosition(self):
        (x,y) = pyautogui.position()
        print('Pos x: {xcord}, Pos y: {ycord} '.format(xcord=x,ycord=y))

    def openFileRecord(self):
        self.file_record = open("keys_record.txt","w")

    def writeFileRecord(self):
        self.record_number = self.record_number + 1

        # Write the numbers of records
        self.file_record.write("\n\n")
        self.file_record.write('RECORD NUMBER {n}\n'.format(n = self.record_number))

        # Write the position
        (x,y) = pyautogui.position()
        s = 'Pos x: {xcord}, Pos y: {ycord} \n'.format(xcord=x,ycord=y)
        self.file_record.write(s)
        self.file_record.write("\n\n")


    def closeFileRecord(self):
        self.file_record.close()


    def clickCertainPosition(self, x, y):
        pyautogui.moveTo(x,y)
        pyautogui.click()

    # Actions openSea Page
    def clickCreateButton(self):
        self.clickCertainPosition(3104,694)

    def clickUploadImageButton(self):
        self.clickCertainPosition(2399,1014)

    def selectImage(self):
        for a in range(self.counter):
            pyautogui.press('down')


    def clickNameButton(self):
        self.clickCertainPosition(2440,1186)

    def pressEnter(self):
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")

    def writeWithKeyboard(self, msg):
        pyautogui.typewrite(msg + "\n")

    def writeName(self):
        self.counter = self.counter + 1
        self.writeWithKeyboard(self.collection_name + " #" + str(self.counter))

    def writePrice(self):
        self.writeWithKeyboard("0.002")

    def writeDescription(self):
        self.writeWithKeyboard(self.collection_description)

    def scrollDown(self,x):
        pyautogui.scroll(-x)

    def clickDescriptionButton(self):
        self.clickCertainPosition(2441,886)

    def clickCollectionButton(self):
        self.clickCertainPosition(2888,1030)

    def clickSelectCollection(self):
        self.clickCertainPosition(2870,1088)

    def selectPolygonChain(self):
        self.clickCertainPosition(2550,979)
        self.clickCertainPosition(2505,1025)

    def createNFT(self):
        self.clickCertainPosition(2320,1207)


    def sellNFT(self):
        self.clickCertainPosition(2796,773)
        self.clickCertainPosition(3008,765)
        time.sleep(2)
        self.clickCertainPosition(2376,943)

    def pastePriceNFT(self):
        pyautogui.hotkey('ctrl', 'v')

        
    

    def clickListNFT(self):
        self.clickCertainPosition(2137,1255)

    def endUpListing(self):
        time.sleep(1)
        self.clickCertainPosition(2397,1060)
        time.sleep(2)
        self.clickCertainPosition(3203,1172)
        time.sleep(1)
        self.clickCertainPosition(2851,781)

        print(' -- NFT {name} #{number} MINTED AND CREATED -- )'.format(name=self.collection_name, number = self.counter))








# Test case purposes
if __name__ == "__main__":
    # Record mouse position
    driver = DriverMoveMouse()
    for a in range(100000):
        time.sleep(0.3)
        driver.clickCreateButton()
        driver.clickUploadImageButton()
        driver.selectImage()
        driver.pressEnter()
        driver.clickNameButton()
        driver.writeName()
        driver.scrollDown(10)
        driver.clickDescriptionButton()
        driver.writeDescription()
        driver.clickCollectionButton()
        driver.clickSelectCollection()
        driver.scrollDown(30)
        driver.selectPolygonChain()
        driver.createNFT()
        time.sleep(5)
        driver.sellNFT()
        driver.pastePriceNFT()
        driver.clickListNFT()
        driver.endUpListing()




