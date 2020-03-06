import unittest
from name_function import getFormattedName

class NamesTestCase(unittest.TestCase):
    #Tests for name_function.py
    def test_first_last_name(self):
        #Do names like 'Janis Joplin' work?
        formattedName = getFormattedName('janis','joplin')
        self.assertEqual(formattedName, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like Wolfgang Amadeus Mozart Work?"""
        formattedName = getFormattedName('wolfgang','mozart','Amadeus')
        self.assertEqual(formattedName, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()