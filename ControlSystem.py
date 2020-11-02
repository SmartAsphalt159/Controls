import time
import Sensors


"""Call when all sensor have been updated"""
def onAllUpdated():
    global last_updated
    _now = time.time()
    _delta_t = last_updated - _now
    last_updated = _now

def find_target_velocity():
    comm_reference = get_comm_ref() #pseudocode
    distance = get_lead_car_delta_distance
    return target_velocity

def motor_value():
    deltav = find_target_velocity() - sensors.get_linear_speed()
    #try to change velocity by deltav

def checkUpdated():


if __name__=="__main__":
    last_updated = time.time()
    sensors = Sensors()
    precision = 1 #cm
