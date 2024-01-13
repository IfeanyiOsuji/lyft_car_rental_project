import unittest
from engine.capulet_engine import CapuletEngine
from car_factory import CarFactory
from datetime import date
from car import Car
from tyre.carrigan_tyre import CarriganTire
from tyre.octoprime_tyre import OctoprimeTyre
from battery.splinder_battery import SplinderBattery

class CarAndTyreTest(unittest.TestCase):
    def test_create_car_with_tyre(self):
        tyre =   CarriganTire([])
        car = Car(None, None, tyre)
        assert(car is not None)

    def test_car_with_carrigantire_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tyre = CarriganTire([0.1, 0.9, 0.8, 0.3])
        car = Car(engine, battery, tyre)
        self.assertTrue(car.needs_service())

    def test_car_with_carrigantire_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tyre = CarriganTire([0.1, 0.3, 0.8, 0.3])
        car = Car(engine, battery, tyre)
        self.assertFalse(car.needs_service())

    def test_car_with_octoprime_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tyre = OctoprimeTyre([0.1, 0.1, 0.01, 0.2])
        car = Car(engine, battery, tyre)
        self.assertTrue(car.needs_service())


    def test_car_with_octoprime_tyre_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tyre = OctoprimeTyre([0.1, 0.1, 0.01, 0.02])
        car = Car(engine, battery, tyre)
        self.assertFalse(car.needs_service())




if __name__ == '__main__':
    unittest.main()
        