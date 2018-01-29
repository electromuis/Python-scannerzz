from scanner import *
from RPLCD import CharLCD
import OPi.GPIO as GPIO

driver = FlowerDriver(
    "abc",
    "http://localhost:8080/check.php",
    CharLCD(
        cols=16,
        rows=2,
        numbering_mode=GPIO.BCM,
        pin_rs=36,
        pin_e=38,
        pins_data=[37,35,33,31]
    )
)

scanner = KeyboardScanner(driver, "Main")
scanner.listen()
