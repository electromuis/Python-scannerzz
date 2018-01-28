from threading import Thread
import keyboard
import requests
import json

class CardData:
    cardId = -1

    def __init__(self, scanner, cardId):
        self.cardId = cardId
        self.scanner = scanner


class Driver:
    def handleData(self, data):
        print data.scanner.name + " :: Card id:" + data.cardId


class CoinDriver(Driver):
    def insertCoin(self):
        print "Coin inserted"

    def checkCardData(self, data):
        return True

    def handleData(self, data):
        if self.checkCardData(data):
            self.insertCoin()


class ItgDriver(CoinDriver):
    def __init__(self, file, coinKey):
        self.coinKey = coinKey
        with open(file) as f:
            content = f.readlines()

        self.ids = [x.strip() for x in content]

    def insertCoin(self):
        keyboard.press(self.coinKey)

    def checkCardData(self, data):
        return data.cardId in self.ids

class FlowerDriver(CoinDriver):
    def __init__(self, token, endpoint):
        self.token = token
        self.endpoint = endpoint

    def checkCardData(self, data):
        try:
            response = requests.post(
                self.endpoint,
                data=json.dumps({
                    'cardId': data.cardId,
                    'token': self.token
                })
            ).json()

            if response.status == 'SUCCESS':
                return True

            return False
        except Exception:
            return False

class Scanner(Thread):
    running = False
    name = ""

    def __init__(self, driver):
        self.__init__(driver, "")

    def __init__(self, driver, name):
        Thread.__init__(self)
        self.driver = driver
        self.name = name
        print "hello"

    def foundCard(self, data):
        if self.driver:
            self.driver.handleData(data)

    def checkCard(self):
        print "checking card"

    def listen(self):
        self.running = True
        while self.running:
            self.checkCard()

    def run(self):
        self.listen()


class KeyboardScanner(Scanner):
    def checkCard(self):
        recorded = keyboard.record(until="enter")
        typed = next(keyboard.get_typed_strings(recorded))
        if typed:
            self.foundCard(CardData(self, typed))
