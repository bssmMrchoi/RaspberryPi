import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

def on():
    try:
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
    except:
        print("error")

def off():
    try:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
    except:
        print("error")
