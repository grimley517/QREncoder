from qr import qrc as qrcode
import unittest
import random

class vstests(unittest.TestCase):
    
    def test1(self):
        with open('sizetestData.txt', 'w') as ofile:
            letters = list('0123456789')
            msg = ''
            self.ver = 0
            while self.ver<41:
                msg = msg + random.choice(letters)
                code = qrcode(msg = msg)
                if self.ver < code.size:
                    ofile.write('msg of length {0} generates a version {1} code \n'.format(len(msg),code.size))
                    self.ver = code.size
                    
        
if __name__ == '__main__':
    unittest.main()