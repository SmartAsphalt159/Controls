import pigpio as IO
import time

class Hall():
    def __init__(self):
        self.last_time = time.time()
        IO.exceptions = False
        self.pi = IO.pi()

        self.cb = self.pi.callback(14, IO.EITHER_EDGE)

        self.pi.set_mode(14, IO.INPUT)


        self.update_time = 1 #s
        self.tally = 0


    def update_tally(self):
        now = time.time()
        self.rps = self.cb.tally()/(now-self.last_time)
        print(self.cb.tally(), self.rps)
        self.last_time = now
        self.cb.reset_tally()


    def loop(self):
        try:
            while True:
                self.update_tally()
                time.sleep(self.update_time)
        except:
            self.pi.stop()
            exit()


        #if 0 on magnet
        #if 1 not on magnet
if __name__ == "__main__":
    print("starting")
    h = Hall()
    h.loop()
