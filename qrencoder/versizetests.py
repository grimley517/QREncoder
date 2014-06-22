from qr import qrc as qrcode
import unittest
import random

class vstests(unittest.TestCase):
    def setUp(self):
        self.letters = list('0123456789')
        
    def test1(self):
        with open('sizetestData.txt', 'w') as ofile:
            msg = ''
            self.ver = 0
            while self.ver<40:
                msg = msg + random.choice(self.letters)
                code = qrcode(msg = msg)
                if self.ver < code.size:
                    ofile.write('msg of length {0} generates a version {1} code \n'.format(len(msg),code.size))
                    self.ver = code.size
                    
    def test2(self):
        code = qrcode('1')
        assert (code.size ==1)
        
    def test3(self):
        msg = ''
        while len(msg) < 3994:
            msg = msg + random.choice(self.letters)
        self.assertRaises(ValueError, qrcode, msg)
            
            
if __name__ == '__main__':
    unittest.main()