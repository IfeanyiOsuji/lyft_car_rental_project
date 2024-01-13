import unittest
from tyre.carrigan_tyre import CarriganTire
from tyre.octoprime_tyre import OctoprimeTyre

class CarriganTyreTest(unittest.TestCase):
    def test_create_carrigan_tyre(self):
        wear_sensors = []
        tyre = CarriganTire(wear_sensors)
        assert(tyre is not None)


    def test_carrigan_tyre_needs_service(self):
        wear_sensors = [0.5, 0.7, 1, 0.2]
        tyre = CarriganTire(wear_sensors)
        self.assertTrue(tyre.needs_service())

    def test_carrigan_tyre_does_not_need_service(self):
        wear_sensors = [0.5, 0.7, 0.1, 0.2]
        tyre = CarriganTire(wear_sensors)
        self.assertFalse(tyre.needs_service())


class OctoprimeTyreTest(unittest.TestCase):
    def test_create_octoprime_tyre(self):
        wear_sensors = []
        tyre = OctoprimeTyre(wear_sensors)
        assert(tyre is not None)

    def test_octoprime_tyre_needs_service(self):
        wear_sensors = [0.01, 0.07, 0.1, 0.2]
        tyre = OctoprimeTyre(wear_sensors)
        self.assertTrue(tyre.needs_service())


    def test_octoprime_tyre_does_not_need_service(self):
        wear_sensors = [0.01, 0.07, 0.01, 0.2]
        tyre = OctoprimeTyre(wear_sensors)
        self.assertFalse(tyre.needs_service())



if __name__ == '__main__':
    unittest.main()

