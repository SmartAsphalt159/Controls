import LidarLibrary
import EncoderLibrary
import math

wheel_radius = 5 #cm
filter_distance = 1000 #cm  #distance of what values it should factor in


class Sensors():
    def __init__(self):
        self.lidar = LidarLibrary.Lidar() #pseudocode
        self.encoder =  EncoderLibrary.Encoder() #pseudocode
        self._rotational_speed = 0
        self._linear_speed = 0
        self._acceleration = 0
        self._leading_car_list = []

    def update_encoder(self,delta_t):
        global wheel_radius
        old_speed = self._linear_speed
        self._rotational_speed = self.encoder.getSpeed() #hz #pseudocode
        self._linear_speed = (self._rotational_speed * 2
                            * math.pi * wheel_radius) #m/s
        self._acceleration = (self._linear_speed-old_speed) / delta_t

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



class LeadingCar():
    """rel_pos, rel_vel are 2D arrays holding x and y values. Lidar is considered origin"""
    def __init__(self, rel_pos, rel_vel,id):
        self.rel_pos = rel_pos #from lidar
        self.rel_vel = rel_vel
        self.id = id
        #maybe chunk of point cloud that

        #add additional machine vision a parameters
