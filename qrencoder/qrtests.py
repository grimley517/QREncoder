from qr import qrc as qrcode
import unittest

class fntests(unittest.TestCase):
    
    def setUp(self):
        self.block = qrcode(size = 0, msg = 'hello', quality = 'M')
        
    def test1(self):
        assert(str(self.block) =='hello') #Test 1 fails - qr object not created, and does not have correct string representation.
    
if __name__ == '__main__':
    unittest.main()