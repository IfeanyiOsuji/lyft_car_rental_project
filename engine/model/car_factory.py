from car import Car
from engine  import Engine

from capulet_engine import CapuletEngine
from splinder_battery import SplinderBattery
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from nubbin_battery import NubbinBattery


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        calliope = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date))
        return calliope
   
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        glissade = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date))
        return glissade
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on)->Car:
        palindrome = Car(engine=SternmanEngine(last_service_date, warning_light_is_on), battery=SplinderBattery(last_service_date, current_date))
        return palindrome
    
    def create_rorscharch(self, current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        rorscharch = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return rorscharch
    
    def create_thovax(self, current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        thovax = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return thovax

