from car import Car
#from engine.engine  import Engine

from engine.capulet_engine import CapuletEngine
from battery.splinder_battery import SplinderBattery
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from tyre.carrigan_tyre import CarriganTire
from tyre.octoprime_tyre import OctoprimeTyre


class CarFactory:
    # Car without Tyre
    @staticmethod
    def create_calliope(last_service_date, current_date, current_mileage, last_service_mileage, wear_sensors=None)->Car:
        calliope = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date), tyre=CarriganTire(wear_sensors))
        return calliope
   
    @staticmethod
    def create_glissade(last_service_date, current_date,current_mileage, last_service_mileage, wear_sensors=None)->Car:
        glissade = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=SplinderBattery(last_service_date, current_date))
        return glissade
    @staticmethod
    def create_palindrome(last_service_date, current_date,warning_light_is_on, wear_sensors=None)->Car:
        palindrome = Car(engine=SternmanEngine(last_service_date, warning_light_is_on), battery=SplinderBattery(last_service_date, current_date), tyre=OctoprimeTyre(wear_sensors))
        return palindrome
    
    @staticmethod
    def create_rorscharch(last_service_date,current_date, current_mileage, last_service_mileage, wear_sensors=None)->Car:
        rorscharch = Car(engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return rorscharch
    @staticmethod
    def create_thovax(last_service_date,current_date, current_mileage, last_service_mileage, wear_sensors=None)->Car:
        thovax = Car(engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date, current_date))
        return thovax
    
    # Car with Tyre

   