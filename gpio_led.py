import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


RED = 3 # 3rd GPIO on the board
INPT = 5
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(INPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def myOnCallBack(INPT):
    print('LED ON')


GPIO.add_event_detect(INPT, GPIO.RISING)
GPIO.add_event_callback(INPT, myOnCallBack)

try:
    while True:
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(0.5) #500 milliseconds
        GPIO.output(RED, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
