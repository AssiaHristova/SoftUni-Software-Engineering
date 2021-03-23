from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def sensor_count(self):
        pass


class Android(Robot):
    def sensor_count(self):
        return 6


class Chappie(Robot):
    def sensor_count(self):
        return 4


def count_robot_snsors(robots: list):
    for robot in robots:
        print(robot.sensor_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_snsors(robots)
