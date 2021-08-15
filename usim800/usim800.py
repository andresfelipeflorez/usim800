# from ATRequests import requests

from usim800.Sms import sms
from usim800.Communicate import communicate
from usim800.Request import request
from usim800.Info import info
from usim800.Call import Call
import serial


class Sim800(communicate):
    TIMMEOUT = 1

    def __init__(self, baudrate, pathToSerial):
        self.port = serial.Serial(pathToSerial, baudrate, timeout=Sim800.TIMMEOUT)
        super().__init__(self.port)
        self.requests = request(self.port)
        self.info = info(self.port)
        self.sms = sms(self.port)
        self.call = Call(self.port)


    def pin_watch_active_call(self, pin_number):
        self.call.pin_watch_active_call(pin_number)
