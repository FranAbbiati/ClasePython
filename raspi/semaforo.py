import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT) 
estado=False
try:
    while estado==False:
        try:
            velE=float(input("Elija la velocidad de espera: "))
            velT=float(input("Elija la velocidad de transicion: "))
            estado=True
            break
        except ValueError:
            print("Escribilo en numeros")
    print("Funcionando. Presione ctrl C para salir.")
    while True:
        GPIO.output(17, True)
        time.sleep(velE)
        GPIO.output(17, False)
        GPIO.output(22, True)
        time.sleep(velT)
        GPIO.output(22, False)
        GPIO.output(27, True)
        time.sleep(velE)
        GPIO.output(27, False)
        GPIO.output(22, True)
        time.sleep(velT)
        GPIO.output(22, False)
except KeyboardInterrupt:
    print("Saliendo...")

finally:
    GPIO.cleanup()