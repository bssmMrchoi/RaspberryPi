import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def on():
    try:
        GPIO.output(8, GPIO.HIGH)
        return "ok"
    except:
        print("on error")
        return "no"

def off():
    try:
        GPIO.output(8, GPIO.LOW)
        return "ok"
    except:
        print("off error")
        return "no"
