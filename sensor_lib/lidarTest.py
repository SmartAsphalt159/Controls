import os
from math import cos, sin, pi, floor
from rplidar import RPLidar
import RPi.GPIO as GPIO
from time import time,ctime



class Lidar():
    header = [
        "time added",
        "angle",
        "strength",
        "distance"
    ]

    def __init__(self):
        PORT_NAME = '/dev/ttyUSB0'
        self.lidar = RPLidar('/dev/ttyUSB0')
        print("Initialized")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.OUT)
        self.lidar.connect()
        self.time_last=0
        self.make_csv()
        self.append_csv(Lidar.header)

    def print_health(self):
        print(self.lidar.health())

    def print_info(self):
        print(self.lidar.info())

    def restart(self):
        self.lidar.reset()
        self.lidar.connect()

    def get_measurements(self):
        try:
            self.lidar.connect()
            iterator = self.lidar.iter_measurments()
            for new_scan, quality, angle, distance in iterator:
                now = time()
                self.append_csv([now,angle,quality,distance])
                print(f"angle: {floor(angle)} \tdistance: {floor(distance)}")
                if distance < 300 and distance > 5:
                    self.time_last = now
                    self.proximity(True)
                    print("tripping")
                    continue

                if now - self.time_last < 0.5:
                    self.proximity(True)
                else:

                    self.proximity(False)


        except KeyboardInterrupt:
            self.lidar.stop()
            self.lidar.disconnect()


    def proximity(self,alert):
        if alert:
            GPIO.output(14,True)
        else:
            GPIO.output(14,False)

    def make_csv(self):
        self.f = open("data.csv", "a")

    def append_csv(self, content):
        formatted = ""
        for index,item in enumerate(content):
            formatted += str(item)
            if index < len(content) - 1:
                formatted += ", "
            else:
                formatted += "\n"

        self.f.write(formatted)

    def close_csv(self):
        self.f.close()

if __name__ == "__main__":
    l = Lidar()
    try:
        l.get_measurements()
    except KeyboardInterrupt:
        l.close_csv()
        exit()
