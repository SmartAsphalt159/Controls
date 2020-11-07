import time
import Sensors

class Controller():
    def __init__(self, p = 1, i = 1, d = 1):
        self.P = p
        self.I = i
        self.D = d
        self._deltax = None
        self._deltax_list = [] #add touple of (deltax,deltat) for integration
        self._deltax_length = 20
        self._deltav = None
        self._delta_t = 1000


    """Call when all sensor have been updated"""
    def on_all_updated(self):
        last_updated
        _now = time.time()
        _delta_t = last_updated - _now
        last_updated = _now

    def update_values(self):
        self.update_deltat()
        self.update_deltax()
        self.update_deltav()

    def update_deltax(self):
        self._deltax = self.get_lead_car_delta_distance()
        self._deltax_list = (self._deltax, self.delta_t)

    def find_target_velocity(self):
        comm_reference = get_comm_ref() #pseudocode
        distance = get_lead_car_delta_distance() #pseudo code from lidar
        deltax = (comm_reference - distance)
        deltav =


        p_val = self.proportional()
        d_val = self.derivative()
        target_velocity = p_val + i_val + d_val

        return target_velocity

    """Following methods are for PID controller"""
    """find proportional value of PID"""
    def proportional(self):
        delta

    """find integral value of PID"""
    def integral(self):
        modifier = (1/self.I)
        sum = 0
        for d,t in self._deltax_list:    #reiman sum of distance between vehicles
            sum += d*t
        return sum*modifier 
    """find derivative value of PID from communications and/or lidar"""
    def derivative(self):
        #depending on: distance from leading car, deltav ...
        #use velocity over communications
        #use velocity from lidar over time
        #use combination of both

    """Create a spline path between lead and following cars and calculate arc length"""
    def get_lead_car_delta_distance(self):
        self.deltax =

    def checkUpdated():


if __name__=="__main__":
    last_updated = time.time()
    sensors = Sensors()
    precision = 1 #cm
