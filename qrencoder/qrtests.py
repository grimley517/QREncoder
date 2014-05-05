from qr import qrc as qrcode
import unittest

class fntests(unittest.TestCase):
    
        
    def test1(self):
        ''' This test checks that a qrcode object can be made
        '''
    
        self.block = qrcode( msg = 'hello', quality = 'M')
        assert(str(self.block) =='hello') #Test 1 fails - qr object not created, and does not have correct string representation.
    
    def test2(self):
        '''This test is to make sure that a block can regognise what type of data it is handling
        
        '''
        msg = 0
        self.block = qrcode (msg = msg)
        assert (self.block.msgtype == 0)#test 2 fails, numeric message is not recognised
    
    def test3(self):
        ''' This test is to ensure that an alphanumeric message is recognised
        
        '''
        msg = 'hi'
        self.block = qrcode (msg = msg)
        assert (self.block.msgtype == 1)# test 3 fails, alphanumeric message in not recongised
    
        
if __name__ == '__main__':
    unittest.main()