from scanner import *
from RPLCD import CharLCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

driver = FlowerDriver(
    "abc",
    "http://24doze.electromuis.nl/test.php",
    32,
    CharLCD(
        cols=16,
        rows=2,
        numbering_mode=GPIO.BOARD,
        pin_rs=36,
        pin_e=38,
        pins_data=[31,33,35,37]
    )
)

scanner = KeyboardScanner(driver, "Main")
scanner.listen()
