import LidarLibrary
import EncoderLibrary
import math

wheel_radius = 5 #cm


class Sensors():
    def __init__(self):
        self.lidar = LidarLibrary.Lidar() #pseudocode
        self.encoder =  EncoderLibrary.Encoder() #pseudocode
        self.rotational_speed = 0
        self.linear_speed = 0
        self.acceleration = 0
        self.leading_car_list = []

    def update_encoder(self):
        global wheel_radius
        self.rotational_speed = self.encoder.getSpeed() #hz #pseudocode
        self.linear_speed = self.rotational_speed*2*math.pi*wheel_radius #m/s
        self

    def get_rotational_speed(self):
        return self.rotational_speed

    def get_linear_speed(self):
        return self.linear_speed

    def update_lidar(self):
        self.lidar.update() #pseudocode

    def interpret_lidar(self):
        lidar_point_cloud = self.lidar.get_pointcloud()#pseudocode




class LeadingCar():
    """rel_pos, rel_vel are 2D arrays holding x and y values. Lidar is considered origin"""
    def __init__(self, rel_pos, rel_vel,id):
        self.rel_pos = rel_pos
        self.rel_vel = rel_vel
        self.id = id
        #add additional machine vision a parameters
