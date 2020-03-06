import unittest
from city_functions import getCityNameandCountry

class cityTestCase(unittest.TestCase):
    """tests for city_functions.py"""
    def test_city_country(self):
        formattedCity = getCityNameandCountry('santiago','chile')
        self.assertEqual(formattedCity, 'Santiago, Chile')
    
    def test_city_country_population(self):
        formattedCity = getCityNameandCountry('santiago', 'chile', 5000000)
        self.assertEqual(formattedCity, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()