from abc import ABC, abstractmethod
from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tyre.tyre import Tyre

class Car(Serviceable, ABC):
    def __init__(self, engine:Engine, battery:Battery, tyre:Tyre=None):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service()



