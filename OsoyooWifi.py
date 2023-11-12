#!/usr/bin/env python
# Olivier Georgeon, 2023.
# This code is used to teach Developmental AI.

import socket
import keyboard
import sys

UDP_IP = "192.168.4.1"
UDP_TIMEOUT = 5  # Seconds


class OsoyooWifi:
    def __init__(self, ip=UDP_IP, port=8888):
        self.IP = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(UDP_TIMEOUT)

    def enact(self, action):
        """ Sending the action string, waiting for the outcome, and returning the outcome bytes """
        outcome = None  # Default status T if timeout
        # print("sending " + action)
        self.socket.sendto(bytes(action, 'utf-8'), (self.IP, self.port))
        try:
            outcome, address = self.socket.recvfrom(512)
        except socket.error as error:  # Time out error when robot is not connected
            print(error)
        return outcome


# Test the wifi interface by controlling the robot from the console
# Provide the Robot's IP address as a launch argument
# py OsoyooWifi.py 192.168.8.242
if __name__ == '__main__':
    _ip = UDP_IP
    if len(sys.argv) > 1:
        _ip = sys.argv[1]
    else:
        print("Please provide your robot's IP address")
    print("Connecting to robot: " + _ip)
    print("Action keys: 1: Turn left, 2: Backward, 3: Turn right, 4: Swipe left, 6: Swipe right, 8: Forward, -: Scan")
    print("Ctrl+C and ENTER to abort")
    osoyoo_wifi = OsoyooWifi(_ip)
    clock = 0
    _action = ""
    while True:
        print("Press action key:")
        _action = keyboard.read_key().upper()
        action_string = '{"clock":' + str(clock) + ', "action":"' + _action + '"}'
        print("Sending packet:", action_string)
        _outcome = osoyoo_wifi.enact(action_string)
        print("Received packet:", _outcome)
        clock += 1
