import unittest
from name_function import getFormattedName

class NamesTestCase(unittest.TestCase):
    #Tests for name_function.py
    def test_first_last_name(self):
        #Do names like 'Janis Joplin' work?
        formattedName = getFormattedName('janis','joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()