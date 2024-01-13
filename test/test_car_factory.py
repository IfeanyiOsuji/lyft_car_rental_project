import unittest
from datetime import date
from car_factory import CarFactory

class CalliopeWithTyreTest(unittest.TestCase):
    def test_calliope_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        wear_sensors = [0.1, 0.9, 0.8, 0.3]
        car = CarFactory.create_calliope(last_service_date, current_date,current_mileage, last_service_mileage, wear_sensors )
        self.assertTrue(car.needs_service())

    def test_calliope_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        last_service_mileage = 0
        wear_sensors = [0.1, 0.7, 0.8, 0.3]
        car = CarFactory.create_calliope(last_service_date, current_date,current_mileage, last_service_mileage, wear_sensors )
        self.assertFalse(car.needs_service())

    def test_palindrome_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        warning_light_is_on = False
        wear_sensors = [0.1, 0.1, 0.1, 0.3]
        car = CarFactory.create_palindrome(last_service_date,current_date, warning_light_is_on, wear_sensors)
        self.assertTrue(car.needs_service())

    def test_palindrome_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        warning_light_is_on = False
        wear_sensors = [0.01, 0.01, 0.01, 0.03]
        car = CarFactory.create_palindrome(last_service_date,current_date, warning_light_is_on, wear_sensors)
        self.assertFalse(car.needs_service())

        
if __name__ == '__main__':
    unittest.main()