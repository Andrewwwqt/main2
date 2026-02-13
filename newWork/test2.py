from motion.core import Waypoint
from math import *


class RobotController:
    def __init__(self):


        start_point = []
        start_point.append(Waypoint([radians(10), radians(10), radians(90), radians(10), radians(90), radians(10)]))
        start_point.append(Waypoint([radians(10), radians(10), radians(90), radians(10), radians(90), radians(10)]))

        
        print(start_point)


RobotController()

