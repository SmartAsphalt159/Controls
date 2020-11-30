import LidarLibrary
import math
import RPi.GPIO as GPIO
import time


filter_distance = 1000 #cm  #distance of what values it should factor in


class Sensors():
    def __init__(self):
        self.esc_pin = 12   #needs to be a pwm output
        self.pwm_frequency = 50 #Hz required for servo and pwm
        self.encoder_pin = 13
        self.servo_pin = 14 #needs to be a pwm output

        self.tally = 0
        self.slots = 20*2 #20 spaces and 40 edges
        self._last_time = time.time()

        self.wheel_radius = 4

        self.lidar = LidarLibrary.Lidar() #pseudocode
        self._rotational_speed = 0
        self._linear_speed = 0
        self._acceleration = 0
        self._leading_car_list = []
        self.status = (True, True, True) #Encoder , lidar, comms
        self.sensor_override = False    #To artificially make sensor fail

        self.initialize_GPIO()

    def initialize_GPIO(self):
        """Initialize GPIO"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.esc_pin, GPIO.OUT)
        GPIO.setup(self.encoder_pin, GPIO.IN)
        GPIO.setup(self.servo_pin, GPIO.OUT)

        """Implement threading callback to increment """
        GPIO.add_event_detect(self.encoder_pin, GPIO.BOTH)
        GPIO.add_event_callback(self.encoder_pin, self.inc_count)

        """Initialize GPIO"""
        self.esc = GPIO.PWM(self.esc_pin, self.pwm_frequency)
        self.servo = GPIO.PWM(self.servo_pin, self.pwm_frequency)

    def stop_pwm(self):
        if self.esc:
            self.esc.stop()
        else:
            print("PWM not initialized")

        if self.servo:
            self.servo.stop()
        else:
            print("PWM not initialized")

    """duty cycle range 0-100"""
    def set_esc(self,duty_cycle):
        self.esc.ChangeDutyCycle(duty_cycle)

    def set_servo(self,duty_cycle):
        self.servo.ChangeDutyCycle(duty_cycle)

    def inc_count(self):
        self.tally += 1

    def reset_count(self):
        self.tally = 0

    #overrides sensor check to test ability when sensors are malfunctioning
    def override_sensor(self, enc, lid, com):
        self.sensor_override = True
        self.status = (enc, lid, com)

    def get_rotations(self):
        count = self.tally
        rotations = count/self.slots
        self.reset_count()
        return rotations

    def update_speed_encoder(self):
        now = time.time()

        old_speed = self._linear_speed
        self._rotational_speed = self.get_rotations() #hz #pseudocode
        self._linear_speed = (self._rotational_speed * 2
                            * math.pi * self.wheel_radius) #m/s
        self._acceleration = (self._linear_speed-old_speed) / delta_t
        self._last_time = now

    def get_rotational_speed(self):
        return self._rotational_speed

    def get_linear_speed(self):
        return self._linear_speed

    def update_lidar(self):
        self.lidar.update() #pseudocode

    """should be quite invloved function with machine vision and tracking objects over time"""
    def interpret_lidar(self):
        lidar_point_cloud = self.lidar.get_pointcloud()#pseudocode #get in polar
        cloud_car_list = find_cars(lidar_point_cloud,
                                    self.lidar.angular_resolution) #pseudocode
        if can_see_car() and not self._leading_car_list:
            self._leading_car_list.append(LeadingCar())

            #return direction of leading car, relative velocity of leading car
            #relative position of leading car,

    def clean(self):
        self.stop_pwm()
        GPIO.cleanup()

"""given point cloud from lidar return lists of where it thinks a car is"""
def find_cars(point_cloud, ang_res):
    cloud_car_list = []
    threshold = 15 #cm #what threshold should be used to find edges
    sobel = [-1, 0, 1]  #can change to other operators

    for i in point_cloud:
        if i > filter_distance:
            point_cloud[i] = filter_distance
    """Edge detection loop"""
    for i, point in enumerate(point_cloud):
        sum = 0
        for j in sobel:
            if i == 0 and j == -1:
                sum += j*point_cloud[len(point_cloud) - 1]
            elif i == len(point_cloud) - 1 and i == 1:
                sum += j*point_cloud[0]
            else:
                sum += j*point_cloud[i+j]

        if sum > threshold:
            edges.append(sum)
        else:
            edges.append(0)

    """loop through and find possible cars using machine vision"""
    return cloud_car_list

class lidar_measurements():
    def __init__(self, time, dirction, location, point_cloud, list, last, next):
        self.time = time
        self.direction = direction #(x,y) touple vector from origin
        self.location = location #(x,y) touple vector from origin
        self.point_cloud = point_cloud
        self.list = list
        self.last = last
        self.next = None

    def add_next(self, next):


class LeadingCar():
    """rel_pos, rel_vel are 2D arrays holding x and y values. Lidar is considered origin"""
    def __init__(self, rel_pos, rel_vel,id):
        self.rel_pos = rel_pos #from lidar
        self.rel_vel = rel_vel
        self.id = id
        #maybe chunk of point cloud that

        #add additional machine vision a parameters
