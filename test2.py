from motion.core import RobotControl, Waypoint
from math import *


class RobotController:
    robot = None
    def __init__(self):
        RobotController.robot = RobotControl(ip= "10.20.6.254")

        self.Connect()

        start_point = []
        start_point.append(Waypoint([radians(10), radians(10), radians(90), radians(10), radians(90), radians(10)]))

        RobotController.robot.addMoveToPointJ(start_point)
        RobotController.robot.play



    @staticmethod
    def Connect():
        if RobotController.robot.connect():
            if RobotController.robot.engage():
                RobotController.robot.manualCartMode()