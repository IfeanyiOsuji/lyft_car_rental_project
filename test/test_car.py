import unittest
from datetime import date

# from engine.model.calliope import Calliope
# from engine.model.glissade import Glissade
# from engine.model.palindrome import Palindrome
# from engine.model.rorschach import Rorschach
# from engine.model.thovex import Thovex

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_date,current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-05-15")
        current_mileage = 0
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date,current_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 0
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date,current_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date,current_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 2)
#         warning_light_is_on = False

#         car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         today = datetime.today();
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_rorscharch(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_rorscharch(today,last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         today = datetime.today();
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = CarFactory.create_rorscharch(today,last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = CarFactory.create_rorscharch(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = today.date().replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         today = datetime.today()
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         today = datetime.today()
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
