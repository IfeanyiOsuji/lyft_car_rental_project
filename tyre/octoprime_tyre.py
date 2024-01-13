from abc import ABC
from tyre.tyre import Tyre

class OctoprimeTyre(Tyre, ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        if self.wear_sensors is None:
            return False
        sum =0
        for i in self.wear_sensors:
            sum += i
        if sum >= 0.3:
            return True
        return False
        


