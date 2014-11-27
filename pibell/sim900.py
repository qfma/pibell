# -*- coding: utf-8 -*-

"""

pibell.sim900

This module provides the object to connect a SIM900 GSM/GPRS modem
via the serial port of a Raspberry Pi

"""

import serial

class Sim900(object):
    """The SIM900 modem adapter for the Raspberry Pi

    """

    def __init__(self, tty="/dev/ttyAMA0", beaups=115200, timeout=0.5):
        self._tty = tty
        self._beaups = beaups
        self._timout = timeout

        self.init_modem(tty, beaups, timeout)


    def init_modem(self, tty, beaups, timeout):
        """Initialises the connection to the modem via a serialport"""

        serialport = serial.Serial(tty, beaups, timeout=timeout)
        serialport.write("AT\r".encode())
        response = serialport.readlines(None)

        if response[-1].decode().strip() == "ERROR":
            raise ValueError("Connection to modem could not be established!")

        self.serialport = serialport

    def call(self, number):

        call_command = "ATD " + str(number) + ";\r"
        print("Calling " + str(number))

        self.serialport.write(call_command.encode())
        response = self.serialport.readlines(None)
        if response[-1].decode().strip() == "ERROR":
            raise ValueError("Phonecall failed!")

