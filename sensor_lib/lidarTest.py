import os
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
import RPi.GPIO as GPIO
from time import time


class Lidar():
    def __init__(self):
        PORT_NAME = '/dev/ttyUSB0'
        self.lidar = RPLidar('/dev/ttyUSB0')
        print("Initialized")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.OUT)
        self.lidar.connect()
        self.time_last=0
        self.lidar.set_pwm()

    def print_health(self):
        print(self.lidar.health)

    def print_info(self):
        print(self.lidar.info)

    def restart(self):
        self.lidar.reset()

    def get_measurements_scan(self):
        try:
            for x, scan in enumerate(self.lidar.iter_scans()):
                for measurement in scan:
                    if measurement[1] < 150 or measurement[1] > 210:
                        print(f"rotation: {x} \tangle: {measurement[1]} distance: {measurement[2]}")
                        if measurement[2] < 300:

                            self.proximity(True)
                        else:
                            self.proximity(False)
        except KeyboardInterrupt:
            self.lidar.stop()
            self.lidar.disconnect()
        except:
            self.lidar.disconnect()
            self.lidar.connect()
            self.get_measurements()

    def get_measurements(self):
        try:
            iterator = self.lidar.iter_measurments()
            for new_scan, quality, angle, distance in iterator:
                now = time()
                if (angle < 150 or angle > 210) and distance > 5:
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
        """except:
            self.lidar.disconnect()
            self.lidar.connect()
            self.get_measurements()"""

    def proximity(self,alert):
        if alert:
            GPIO.output(14,True)
        else:
            GPIO.output(14,False)
"""
if __name__ == "__main__":
    try:


    except KeyboardInterrupt:
        print("stop")

    finally:
        l.lidar.stop()
        """
