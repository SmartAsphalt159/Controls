import RPi.GPIO as IO
import time

class Servo():
    def __init__(self):
        self.last_time = time.time()
        IO.setmode(IO.BOARD)

        IO.setup(32,IO.OUT)
        self.pwm = IO.PWM(32, 50)
        self.pwm.start(0)

    def loop(self):
        try:
            while True:
                inp = input()
                self.pwm.ChangeDutyCycle(self.format(float(inp)))
        except:
            self.pwm.stop()
            IO.cleanup()
            exit()

    def format(self, val): #-10 => 8.5 10=>5.5
        if val < -10:
            return 8.5
        elif val > 10:
            return 5.5
        else:
            return val*3/20 + 7

    def sweep(self):
        try:
            val = -10
            inv = 0.05

            while True:
                if val < -10:
                    inv = 0.05
                elif val > 10:
                    inv = -0.05

                val = val + inv

                self.pwm.ChangeDutyCycle(self.format(float(val)))
                time.sleep(0.01)
        except:
            self.pwm.stop()
            IO.cleanup()
            exit()

        #if 0 on magnet
        #if 1 not on magnet
if __name__ == "__main__":
    print("starting")
    s = Servo()
    s.sweep()
