from abc import ABC
from tyre.tyre import Tyre
class CarriganTire(Tyre, ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        if self.wear_sensors is None:
            return False
        for i in self.wear_sensors:
            if i >= 0.9:
                return True
        return False
        
