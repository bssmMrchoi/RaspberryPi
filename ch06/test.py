import RPi.GPIO as GPIO
from time import sleep

MAX_DUTY = 12
MIN_DUTY = 3
pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

servo = GPIO.PWM(pin, 50) # pin을 PWM 모드 50Hz로 사용
servo.start(0) # DUTY 가 0이라 서보는 동작하지 않음

def setServoPos(degree):
    if degree > 180:
        degree -= 180

    duty = MIN_DUTY + (degree * (MAX_DUTY - MIN_DUTY) / 180.0)
    print("degree : {} to {}(duty)".format(degree, duty))

    servo.ChangeDutyCycle(duty)

def stopServo():
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setServoPos(0)
    sleep(1)
    setServoPos(90)
    sleep(1)
    setServoPos(50)
    sleep(1)
    setServoPos(120)
    sleep(1)
    setServoPos(190)
    sleep(1)
    setServoPos(180)
    sleep(1)

    servo.stop()
    GPIO.cleanup()
