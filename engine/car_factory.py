from car import Car
#from engine.engine  import Engine

from engine.capulet_engine import CapuletEngine
from battery.splinder_battery import SplinderBattery
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        calliope = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date))
        return calliope
   
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        glissade = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date))
        return glissade
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on)->Car:
        palindrome = Car(engine=SternmanEngine(last_service_date, warning_light_is_on), battery=SplinderBattery(last_service_date, current_date))
        return palindrome
    
    @staticmethod
    def create_rorscharch(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        rorscharch = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return rorscharch
    @staticmethod
    def create_thovax(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        thovax = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return thovax

