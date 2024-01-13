from abc import ABC

#from car import Car
from engine.engine import Engine


# class CapuletEngine(Car, ABC):
#     def __init__(self, last_service_date, current_mileage, last_service_mileage):
#         super().__init__(last_service_date)
#         self.current_mileage = current_mileage
#         self.last_service_mileage = last_service_mileage

#     def engine_should_be_serviced(self):
#         return self.current_mileage - self.last_service_mileage > 30000

class CapuletEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        bool =  (self.current_mileage - self.last_service_mileage) > 30000
        print(bool)
        return bool
