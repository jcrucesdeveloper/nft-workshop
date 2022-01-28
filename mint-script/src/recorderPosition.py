from driverMoveMouse import DriverMoveMouse
import time, keyboard


# Test case purposes
if __name__ == "__main__":

    # Record mouse position
    driver = DriverMoveMouse()
    driver.openFileRecord()

    while True:
        time.sleep(0.03)
        driver.printPosition()
        # Record key position
        if keyboard.is_pressed("r"):
            print("RECORDED ")
            driver.writeFileRecord()

    driver.closeFileRecord()









