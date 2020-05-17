import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin_trig =16
pin_echo =18
ledPin = 23

GPIO.setup(pin_trig, GPIO.OUT)
GPIO.setup(pin_echo, GPIO.IN)
GPIO.setup(ledPin , GPIO.OUT)

GPIO.output(pin_trig, False)

pwm = GPIO.PWM(ledPin, 100)
pwm.start(0)

time.sleep(2)

try:
    while(True):
        GPIO.output(pin_trig,True)
        time.sleep(0.00001)
        GPIO.output(pin_trig,False)

        while GPIO.input(pin_echo)==0:
            start = time.time()

        while GPIO.input(pin_echo)==1:
            stop = time.time()

        pDuration = stop - start

        distance = pDuration * 17150

        distance = round(distance,2)
        time.sleep(1)

        if distance <= 100:
            rem = 100 - distance
        else:
            rem = 0

        pwm.ChangeDutyCycle(rem)
        time.sleep(1)

        print "Distance to the sensor: ",distance
        print "Duty Value: ",rem,"\n"

except KeyboardInterrupt:
    pass


pwm.stop()
GPIO.cleanup()
