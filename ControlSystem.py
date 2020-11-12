import time
import Sensors

class Controller():
    def __init__(self, p = 1, i = 1, d = 1, k = 1, sensors):
        self.P = p
        self.I = i
        self.D = d
        self.Kp = k
        self.pwm_scale =  1000  #pulse width(ms)/speed(m/s)
        self._pid_list = [] #add touple of (pid_val,time) for integration
        self._pid_length = 20
        self.sensors = sensors  #object that interacts with the sensors
        self.pos_ref = 20 #cm reference position
        self.operational_sensors = (True, True, True) #Encoder (crit), lidar(red), comms (red)

    def control_loop(self):
        return 0

    def update_ref(self):
        self.pos_ref = get_comm_ref() #pseudocode


    def positional_error(self):


        if()
        distance = get_lead_car_delta_distance() #pseudo code from lidar


        return

    """Following methods are for PID controller"""
    def pid_controller(pid_input):
        time = time.time()
        _pid_list.append((pid_input,time))
        if len(_pid_list) > self._pid_length:
            del _pid_list[0]

        pid_val = self.proportional(pid_input) +
                  self.integral() +
                  self.derivative()

        return pid_val

    """find proportional value of PID"""
    def proportional(self, pid_input):
        p_val = pid_input * self.P
        return p_val

    """find integral value of PID"""
    def integral(self):
        if not self._pid_list:
            return 0

        modifier = (1/self.I)
        sum = 0

        for x,(pid,t) in self._pid_list:    #reiman sum of distance between vehicles
            sum += pid * (t - self._pid_list[x][1])   #calculate deltat * pid val

        i_val = sum * modifier
        return i_val

    """find derivative value of PID from communications and/or lidar"""
    def derivative(self):
        if not self._pid_list:
            return 0

        d_val = (self._pid_list[-1][0]-self._pid_list[-2][0])
                /(self._pid_list[-1][1]-self._pid_list[-2][1])
        d_val =* self.D

        return d_val

    """convert value from PID controller to pwm"""
    def pid_to_pwm(self,pid_val):

        return pwm_signal

    """Create a spline path between lead and following cars and calculate arc length"""
    def get_lead_car_delta_distance(self):


    def get_v_of_lead(self):




if __name__=="__main__":
    last_updated = time.time()
    sensors = Sensors()
    precision = 1 #cm
