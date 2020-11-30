import pigpio as IO
import time

print("starting")

class Controller:
    def __init__(self):
        IO.exceptions = False

        self.pi = IO.pi()
        self.pi.set_mode(12, IO.OUTPUT)
        self.pi.set_mode(3, IO.INPUT)
        self.pi.set_PWM_frequency(12,20000)
        self.pi.set_PWM_dutycycle(12,0)
        self.motor_speed(0)

        self.cb = self.pi.callback(3, IO.EITHER_EDGE)
        self.slots = 20 #20 slots in encoder
        self.last_time = time.time()
        self.target_speed = 0
        self.speed = 0
        self.target_duty_cycle = 0
        #self.mes_speed = 0
        self.p = 5
        self.i = 0.001

        #self.last_values = []
        #self.last_length = 4

        self.integrator = []    #(val,time)
        self.length = 10

    def stop(self):
        self.motor_speed(0)
        #self.pi.stop()


    def motor_speed(self, duty_cycle):  #0-255
        self.pi.set_PWM_dutycycle(12, duty_cycle)

    def update_tally(self):
        now = time.time()
        print(self.cb.tally())
        self.sample_rate = int(self.cb.tally()) / (2 * (now - self.last_time))
        self.speed = self.sample_rate/self.slots
        self.last_time = now
        self.cb.reset_tally()


    def speed_control(self, ts):
        self.target_speed = ts
        try:
            while True:
                self.update_tally()
                now = time.time()

                #self.last_values.append(self.mes_speed)
                #if len(self.last_values) > self.last_length:
                #    del self.last_values[0]

                #s = 0
                #for k in self.last_values:
                #    s += k

                #self.speed = s/len(self.last_values)
                val = (self.target_speed - self.speed)
                p = self.p * val

                self.integrator.append((val,now))
                if len(self.integrator) > self.length:
                    del self.integrator[0]

                sum = 0
                for x,(pid,t) in enumerate(self.integrator):    #reiman sum of distance between vehicles
                    if  x - 1 >= 0:
                        sum += pid * (t - self.integrator[x-1][1])

                i = (1/self.i)*sum

                self.target_duty_cycle = i + p
                act = self.target_duty_cycle
                if self.target_duty_cycle > 200:
                    self.target_duty_cycle = 200
                elif self.target_duty_cycle < 100:
                    self.target_duty_cycle = 100

                self.motor_speed(self.target_duty_cycle)
                print(f"speed: {self.speed} val: {val} p: {p} i: {i} actual: {act} ds: {self.target_duty_cycle}")
                time.sleep(.01)
        except KeyboardInterrupt:
            self.stop()

#test

if __name__ == "__main__":
    print("starting")
    c = Controller()
    c.motor_speed(150)
    try:
        while True:
            print("In loop")
            sleep(1)
            c.print_tally()

    except KeyboardInterrupt:
        c.stop()
