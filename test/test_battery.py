import unittest
from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery
from datetime import date

class SplinderBatteryTest(unittest.TestCase):
    def test_splinder_battery_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        
        battery = SplinderBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_splinder_battery_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        
        battery = SplinderBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class NubbinBatteryTest(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())




if __name__ == '__main__':
    unittest.main()