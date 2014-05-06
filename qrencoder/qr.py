import math
class qrc(object):
    sizemin = 1
    sizemax = 40
    sizeListChar = [26,44,70,100,134,172,196,242,292,346,404,466,532, 582, 655,733, 
    835,901,991,1085,1156,1258,1364, 1474, 1588, 1706, 1828, 1921, 2051, 2185, 
    2323, 2465, 2611, 2761, 2876, 3034, 3196, 3362, 3532, 3706]
    
    def __init__ (self, msg = '', quality = 'L'):
        self.msg = str(msg)
        self.quality = quality
        if self.msg.isdigit():
            self.msgtype = 0
            self.getSizeNumeric()
        elif self.msg.isalnum():
            self.msgtype = 1
        else:
            raise TypeError('message type not recognised')
    
    def getSizeNumeric(self):
        sizeListBin = []
        for i,n in enumerate(self.sizeListChar, start =1):
            sizeBin = n*8
            sizeBin = sizeBin -14
            if i>9:
                sizeBin = sizeBin -2
            if i>26:
                sizeBin = sizeBin -2
            sizeListBin.append(sizeBin)
        D = len(self.msg)
        
        R = D%3
        if R == 1:
            R = 4
        elif R==2:
            R = 7
        bitsRequired = math.ceil(10 *(D/3)+R)#this might be better as a floor - check edge cases.
        bitsRequired = int(bitsRequired)
        ver = 1
        for size in sizeListBin:
            if bitsRequired > size:
                ver +=1
        self.size = ver
        
        
        
    def __repr__(self):
        return self.msg