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
        
        return self._engine_needs_service(self.engine) or self._battery_needs_service(self.battery) or self._tyre_needs_service(self.tyre)
    
    def _engine_needs_service(self, engine:Engine):
        if engine is None:
            return False
        return engine.needs_service()
    
    def _battery_needs_service(self, battery:Battery):
        if battery is None:
            return False
        return battery.needs_service()
    
    def _tyre_needs_service(self, tyre:Tyre):
        if tyre is None:
            return False
        return tyre.needs_service()
    





