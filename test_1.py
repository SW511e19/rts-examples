import ev3dev.ev3 as ev3
import time 

def runBackMotor():
    backMotor.speed_sp = -300
    backMotor.run_forever()
    time.sleep(1.1)
    backMotor.stop()

def runFrontMotor():
    frontMotor.speed_sp = -185
    frontMotor.run_forever()
    time.sleep(1.1)
    frontMotor.stop()

def pushCard():
    pushMotor.speed_sp = -120
    pushMotor.run_forever()
    time.sleep(3)
    pushMotor.stop()

pushMotor = ev3.MediumMotor('outB')
backMotor = ev3.LargeMotor('outA')
frontMotor = ev3.LargeMotor('outC')

for lp in range(2):
    runBackMotor()
    time.sleep(4)
    runFrontMotor()
    time.sleep(4)
    pushCard()
    time.sleep(4)
