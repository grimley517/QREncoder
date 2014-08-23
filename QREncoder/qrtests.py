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
    
    def test4(self):
        '''This test checks that the version number chosen for a very short messgae in 1'''
        msg = 123
        expver = 1
        self.block = qrcode(msg = msg)
        assert (self.block.size == expver)#Test 4 fails, short message version not 1
        
    def test5(self):
        ''' simple integrity test for the list of block sizes'''
        self.block = qrcode(msg = '0')
        numberOfVersions = 40
        assert (len(self.block.sizeList)==numberOfVersions)#test5 fails - data items not correct
        for block in self.block.sizeList:
            assert len(block) ==4 #Test 5 Fails - A block in the version size list does not have 4 items
        
if __name__ == '__main__':
    unittest.main()
