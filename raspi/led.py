import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

try:
    print("LED funcionando. Presiona ctrl C para salir")
    while True:
        GPIO.output(27, True)
        time.sleep(1)
        GPIO.output(27, False)
        time.sleep(1)
except KeyboardInterrupt:
    print("Saliendo...")
finally:
    GPIO.cleanup()